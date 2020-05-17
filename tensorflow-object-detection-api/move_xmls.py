import glob
import os
import argparse
import time

""" Moves corresponding xmls from the current working directory to the input directory """

parser = argparse.ArgumentParser()
parser.add_argument("input", help="path to the directory containing the images", nargs='?', default='.')
args = parser.parse_args()


images_folder_path = args.input
jpg_fnames = glob.glob(os.path.join(images_folder_path,'*.jpg'))

for jpg_fname in jpg_fnames:
	xml_fname = jpg_fname.split('.')[0] + '.xml'
	xml_fname = xml_fname.split('/')[-1]
	# print(xml_fname)
	# print(os.path.join(os.getcwd(), images_folder_path,xml_fname))
	# print(os.path.isfile(os.path.join(os.getcwd(), images_folder_path,xml_fname)))
	# time.sleep(5)
	if not os.path.isfile(os.path.join(os.getcwd(), images_folder_path, xml_fname)):
		os.system('cp -v {} {}'.format(xml_fname,images_folder_path))
