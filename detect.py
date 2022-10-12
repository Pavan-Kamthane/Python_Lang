import numpy as np
import cv2

# width and height
w = 1280
h = 720


top_right = (725, 455)
top_left = (555, 455)
botom_right = (1280, 680)
botom_left = (0, 680)

# Source
src = np.float32([[top_right],[top_left],[botom_right],[botom_left]])
src2 = np.float32([[top_right],[top_left],[botom_left],[botom_right]])

# Destination
dst = np.float32([[w,0],[0,0],[w,h],[0,h]])

def warped(img, top_right, top_left, botom_right, botom_left):
    img_size = (img.shape[1], img.shape[0])
    src = np.float32([[top_right], [top_left], [botom_right], [botom_left]])
    w, h = img.shape[1], img.shape[0]
    dst = np.float32([[w, 0], [0, 0], [w, h], [0, h]])

    M = cv2.getPerspectiveTransform(src, dst)
    # get inverse matrix
    Minv = cv2.getPerspectiveTransform(dst, src)
    # warp original image
    warped = cv2.warpPerspective(img, M, img_size, flags=cv2.INTER_LINEAR)

    return warped, Minv


def color_and_gradient_threshold(img):
    hls = cv2.cvtColor(img, cv2.COLOR_RGB2HLS)
    s_channel = hls[:, :, 2] 

    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    # Sobel x
    sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0)  
    abs_sobelx = np.absolute(sobelx)
    scaled_sobel = np.uint8(255 * abs_sobelx / np.max(abs_sobelx))  

    # Threshold x gradient
    thresh_min = 20
    thresh_max = 100
    sxbinary = np.zeros_like(scaled_sobel) 
    sxbinary[(scaled_sobel >= thresh_min) & (scaled_sobel <= thresh_max)] = 1

    # Threshold color channel
    s_thresh_min = 170
    s_thresh_max = 255
    s_binary = np.zeros_like(s_channel) 
    s_binary[(s_channel >= s_thresh_min) & (s_channel <= s_thresh_max)] = 1

    # Combine the two binary thresholds
    combined_binary = np.zeros_like(sxbinary)
    combined_binary[(s_binary == 1) | (sxbinary == 1)] = 1

    return combined_binary


def binary(img):
    global objpoints
    global imgpoints
    global top_right
    global top_left
    global botom_right
    global botom_left

    # Perspective Transform
    result, Minv = warped(img, top_right, top_left, botom_right, botom_left)

    # Aplying Thresholds
    result = color_and_gradient_threshold(result)

    return result, Minv

def fitlines(binary_warped):

    histogram = np.sum(binary_warped[int(binary_warped.shape[0] / 2):, :], axis=0)
  
    out_img = np.dstack((binary_warped, binary_warped, binary_warped)) * 255

  
    midpoint = np.int32(histogram.shape[0] / 2)
    leftx_base = np.argmax(histogram[:midpoint])
    rightx_base = np.argmax(histogram[midpoint:]) + midpoint

 
    nwindows = 9

    window_height = np.int32(binary_warped.shape[0] / nwindows)
   
    nonzero = binary_warped.nonzero()
    nonzeroy = np.array(nonzero[0])
    nonzerox = np.array(nonzero[1])

    leftx_current = leftx_base
    rightx_current = rightx_base

    margin = 100

    minpix = 50
  
    left_lane_inds = []
    right_lane_inds = []

    for window in range(nwindows):
        win_y_low = binary_warped.shape[0] - (window + 1) * window_height
        win_y_high = binary_warped.shape[0] - window * window_height
        win_xleft_low = leftx_current - margin
        win_xleft_high = leftx_current + margin
        win_xright_low = rightx_current - margin
        win_xright_high = rightx_current + margin

        good_left_inds = ((nonzeroy >= win_y_low) & (nonzeroy < win_y_high) & (nonzerox >= win_xleft_low) & (
                    nonzerox < win_xleft_high)).nonzero()[0]
        good_right_inds = ((nonzeroy >= win_y_low) & (nonzeroy < win_y_high) & (nonzerox >= win_xright_low) & (
                    nonzerox < win_xright_high)).nonzero()[0]

        left_lane_inds.append(good_left_inds)
        right_lane_inds.append(good_right_inds)

        if len(good_left_inds) > minpix:
            leftx_current = np.int32(np.mean(nonzerox[good_left_inds]))
        if len(good_right_inds) > minpix:
            rightx_current = np.int32(np.mean(nonzerox[good_right_inds]))


    left_lane_inds = np.concatenate(left_lane_inds)
    right_lane_inds = np.concatenate(right_lane_inds)

 
    leftx = nonzerox[left_lane_inds]
    lefty = nonzeroy[left_lane_inds]
    rightx = nonzerox[right_lane_inds]
    righty = nonzeroy[right_lane_inds]


    if len(leftx) == 0:
        left_fit = []
    else:
        left_fit = np.polyfit(lefty, leftx, 2)

    if len(rightx) == 0:
        right_fit = []
    else:
        right_fit = np.polyfit(righty, rightx, 2)


    ploty = np.linspace(0, binary_warped.shape[0] - 1, binary_warped.shape[0])

    return left_fit, right_fit, out_img, lefty, leftx, righty, rightx, ploty


def draw_lane(img, warped, left_fit, right_fit, ploty, Minv):

    warp_zero = np.zeros_like(warped).astype(np.uint8)
    color_warp = np.dstack((warp_zero, warp_zero, warp_zero))

    left_fitx = left_fit[0] * ploty ** 2 + left_fit[1] * ploty + left_fit[2]
    right_fitx = right_fit[0] * ploty ** 2 + right_fit[1] * ploty + right_fit[2]


    pts_left = np.array([np.transpose(np.vstack([left_fitx, ploty]))])
    pts_right = np.array([np.flipud(np.transpose(np.vstack([right_fitx, ploty])))])  
  

    pts = np.hstack((pts_left, pts_right))

    
    cv2.fillPoly(color_warp, np.int_([pts]), (0, 255, 0))


    newwarp = cv2.warpPerspective(color_warp, Minv, (img.shape[1], img.shape[0]))

    result = cv2.addWeighted(img, 1, newwarp, 0.3, 0)

    return result



cap = cv2.VideoCapture("Videos\project_video.mp4")
i = 0
while(cap.isOpened()):
    _, frame = cap.read() 
    if frame is None:
        break
    frame = frame.astype('uint8')
   
    if i == 0:
        i = 1
        binary_warped, Minv = binary(frame)

        left_fit, right_fit, out_img, lefty, leftx, righty, rightx, ploty = fitlines(binary_warped)

        result_lane = draw_lane(frame, binary_warped, left_fit, right_fit, ploty, Minv)

        cv2.imshow("Road Lane Line Detection", result_lane)
    else :
        i = 0
        cv2.imshow("Road Lane Line Detection", result_lane)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
