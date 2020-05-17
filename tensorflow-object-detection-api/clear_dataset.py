import os
import glob
import argparse
import time

""" Clears an annotation directory created by dataset frames and labelImg output xmls
	It is usefull when you have a lot of frames inside your dataset folder but you do not want to annotate them all for some reason
	So after the annotation job is done you run this script to move out the unwanted frames """

parser = argparse.ArgumentParser()
parser.add_argument("input", help="path to folder containing the iamges and annotation files", nargs='?', default='.')
args = parser.parse_args()

images_folder_path = args.input
jpg_fnames = glob.glob(os.path.join(images_folder_path, '*.jpg'))
other_folder_path = 'unwanted_frames'
os.system('mkdir -p {}'.format(other_folder_path))

for jpg_fname in jpg_fnames:
    xml_fname = jpg_fname.split('.')[0] + '.xml'
    # print(xml_fname)
    # time.sleep(5)
    if not os.path.isfile(xml_fname):
        os.system('mv -v {} {}'.format(jpg_fname, other_folder_path))
