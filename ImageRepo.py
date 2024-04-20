"""
Module responsible for housing the ImageRepo class
"""
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as img
import math

class ImageRepo():
	"""
	Represents the interface to the project's image repository.
	Holds reference to every ca	
	"""

	def __init__(self) -> None:
		self.data_df = pd.read_csv("./metadata/img_data.csv",sep=';')
		self.indexed_df = self.data_df.set_index("img")
		data_by_class = {}

		for row in self.data_df.values:
			img_name = row[0]
			background = row[1]
			light = row[2]
			labels = row[-1]

			for label in eval(labels):
				if label not in data_by_class:
					data_by_class[label] = {"images": [],"backs": [],"lights": []}
				
				label_data = data_by_class[label]

				if img_name not in label_data["images"]:
					label_data["images"].append(img_name)

					if background not in label_data["backs"]:
						label_data["backs"].append(background)
					
					if light not in label_data["lights"]:
						label_data["lights"].append(light)
		
		self.data_by_class = data_by_class

	def get_images_with_class(self, class_label):
		"""
		Retrieves the names of every image containing the
		given class label.
		"""

		return self.data_by_class[class_label]["images"]

	def get_image_labels(self, image):
		"""
		Returns a list with every class label appliable to the 
		given image
		"""
	
		return self.indexed_df.loc[image]["labels"]

	def draw_whole_database(self,cols=10):
		"""
		Draws every image in the database in a matrix with cols columns
		"""

		cols = 10
		rows = math.ceil(len(self.data_df)/10)

		draw_image_grid(self.data_df["img"].values,rows,cols)

	def draw_class_samples(self,label,samples=None,rows=2):
		"""
		Draws a couple of images with the given label
		"""

		images = self.data_by_class[label]["images"]
		if samples is not None:
			if samples > len(images):
				raise ValueError("Too many samples requested")
			images = images[:samples]
		
		cols = math.ceil(len(images)/rows)
		draw_image_grid(images,rows,cols)
	
	def draw_every_class(self):
		"""
		Draws an image of every class in the database
		"""

		images = []
		titles = []
		for label in self.data_by_class:
			titles.append(label)
			label_data = self.data_by_class[label]
			images.append(label_data["images"][0])
		
		cols = 5
		rows = math.ceil(len(images)/cols)
		draw_image_grid(images,rows,cols,titles=titles)

	def print_repo_stats(self):
		"""
		Prints a table containing the repo's basic statistics
		"""
	
	def print_class_based_info(self):
		"""
		Prints a table containing info on the statistics for
		every class on the repository
		"""

def draw_image_grid(images,rows,cols,titles=None):
	"""
	Draws a grid of images
	"""

	_, axs = plt.subplots(rows,cols, figsize=(2*cols, (20/12) * rows))
	i,j = 0,0
	for k in range(len(images)):
		image = images[k]

		with open("./images/" + image,"rb") as img_file:
			axs[i,j].imshow(img.imread(img_file))
		if titles is not None:
			axs[i,j].set_title(titles[k])
		axs[i,j].axis('off')

		j +=1 
		if j == cols:
			j = 0
			i = i + 1 
			
	while j < cols and i < rows:
		axs[i,j].axis('off')
		j +=1 
		
	plt.show()