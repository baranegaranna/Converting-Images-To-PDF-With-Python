from PIL import Image
from msvcrt import getch
from os     import listdir, mkdir, rename, path

converted_images_folder = "./converted images"

def opening_image( image_name ):
	return( Image.open(image_name).convert('RGB') )
	# opening images


def moving_images( image_name ):
	# moving images

	name, extention = path.splitext(image_name)
	# get name and extention
	
	try:
		mkdir(converted_images_folder)
		# creating a folder for converted images
		
	except OSError:
		pass

	try:
		rename("./{}".format( image_name ), "{}/{}".format( converted_images_folder, image_name ))
		# moving file 

	except FileExistsError:
		# choosing a different name if a file with same name exists in folder 

		i = 1

		while True:
			try:
				rename(image_name, "{}/{} ({}) .{}".format( converted_images_folder, name, i, extention ))

			except FileExistsError:
				i += 1

			else:
				break
	return None



def main():
	images_name = [i for i in listdir('.') if i.endswith('.jpg') or i.endswith('.png') or i.endswith('.jpeg') ]
	# finding all images in file directory

	images = list(map( opening_image, images_name ))
	# opening images

	# for i in images:
	# 	 i.show()
	# if you uncomment this part it'll show images one bye one

	name = input('Enter name to continue:\t')
	# getting pdf file name

	if len(images) != 0:
		
		images[0].save('{}.pdf'.format(name), 'PDF', resolution=100.0, save_all=True, append_images=images[1:])
		# converting all images to pdf
		
		print("Number of pages:\t%d" %len(images) )
		# showing number of pages

		for i in images_name:
			moving_images(i)
			# moving images


	else:
		print("No image were found!\n")

	getch()



if __name__ == '__main__':
	main()

