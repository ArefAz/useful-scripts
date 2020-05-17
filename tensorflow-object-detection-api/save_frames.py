import os
import cv2
import argparse 
import glob
import time

""" Saves frames of camera input or a video file in 'images' directory every "step" frames.
    You can run this script multiple times on different videos and the output will get appended to the directory.   """

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="camera device ID (0,1, etc.), or path to video file (default: -1)", nargs='?',
                        default='-1')
    parser.add_argument('--name','-n',help='an arbitrary name just in case of preventing filename conflicts',required=True)
    parser.add_argument('--step','-s',help='frame step', default='10')
    args = parser.parse_args()
    video_file = args.input
    user_name = args.name
    step = int(args.step)
    cap = cv2.VideoCapture(video_file)
    os.system('mkdir -p images')
    main_dir = os.getcwd()
    search_dir = os.path.join(main_dir, "images")
    os.chdir(search_dir)
    images_fnames = filter(os.path.isfile, os.listdir(search_dir))
    images_fnames = [os.path.join(search_dir, f) for f in images_fnames]  # add path to each file
    images_fnames.sort(key=lambda x: os.path.getmtime(x))
    os.chdir(main_dir)
    if len(images_fnames):
        print('last saved image: ' + images_fnames[-1])
        img_num = int(images_fnames[-1].split('_')[-1].split('.')[0]) + 1
        time.sleep(1.5)
    else:
        img_num = 0


    go = 1
    itr = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print('##'*20 +'End of File' + '##'*20)
            break

        cv2.imshow('frame', frame)
        cv2.waitKey(1)
        key = cv2.waitKey(go) & 0xFF
        if key == ord('q'):
        	cv2.destroyAllWindows()
        	break
        if key == ord(' '):
            go = 1 - go
        if key == ord('f'):  # frame by frame
            go = 0
        if chr(key) in list('123456789'):  # skip 10-90 seconds
            for skip in range(int(chr(key)) * 10 * 30):
                cap.grab()
        # if key == ord('s'):
        if itr == step:
        	itr = 0
        	cv2.imwrite(os.path.join('images','{}_img_{}.jpg').format(user_name,img_num), frame)
        	img_num += 1
        	print('image {} saved to images'.format('{}_img_{}.jpg'.format(user_name,img_num)))

        itr += 1
    exit()
