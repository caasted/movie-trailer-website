# media.py
# Chris Aasted
# 2016-09-09

import webbrowser

class Movie(): # class
	"""This class provides a way to store movie-related information"""
	
	VALID_RATINGS = ['G', 'PG', 'PG-13', 'R'] # A class variable
	# Uppercase denotes this is also a constant (doesn't change often, or ever)

	def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
		# This is the class constructor where instance variables get initalized
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube

	def show_trailer(self):
		# This method opens an instance's movie trailer in the default web browser
		webbrowser.open(self.trailer_youtube_url)

