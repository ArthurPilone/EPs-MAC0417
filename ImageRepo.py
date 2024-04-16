"""
Module responsible for housing the ImageRepo class
"""

class ImageRepo():
	"""
	Represents the interface to the project's image repository.
	Holds reference to every ca	
	"""

	def get_images_with_class(self, class_label):
		"""
		Retrieves the names of every image containing the
		given class label.
		"""

	def get_image_classes_labels(self, image):
		"""
		Returns a list with every class label appliable to the 
		given image
		"""
	
	def print_repo_stats(self):
		"""
		Prints a table containing the repo's basic statistics
		"""
	
	def print_class_based_info(self):
		"""
		Prints a table containing info on the statistics for
		every class on the repository
		"""