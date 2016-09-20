# entertainment_center.py
# Chris Aasted
# 2016-09-09

import media
import fresh_tomatoes

# Movies and their information to load on the webpage
toy_story = media.Movie("Toy Story", "A story of a boy and his toys that come to life", 
	"http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", 
	"https://www.youtube.com/watch?v=vwyZH85NQC4")

avatar = media.Movie("Avatar", "A marine on an alien planet", 
	"http://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg", 
	"https://www.youtube.com/watch?v=-9ceBgWV8io")

school_of_rock = media.Movie("School of Rock", "Using rock music to learn",
	"http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg", 
	"https://www.youtube.com/watch?v=3PsUJFEBC74")

ratatouille = media.Movie("Ratatouille", "A rat is a chef in Paris", 
	"http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg", 
	"https://www.youtube.com/watch?v=c3sBBRxDAqk")

midnight_in_paris = media.Movie("Midnight in Paris", "Going back in time to meet authors", 
	"http://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg", 
	"https://www.youtube.com/watch?v=atLg2wQQxvU")

hunger_games = media.Movie("Hunger Games", "A really real reality show", 
	"http://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg", 
	"https://www.youtube.com/watch?v=PbA63a7H0bo")

event_horizon = media.Movie("Event Horizon", 
	"A rescue crew investigates a space ship that reappears after being lost for seven years", 
	"https://upload.wikimedia.org/wikipedia/en/8/8c/Event_horizon_ver1.jpg", 
	"https://www.youtube.com/watch?v=7l-1RYrJNoM")

underworld = media.Movie("Underworld", 
	"It tells the story of Selene (Kate Beckinsale), a vampire who works as a Death Dealer, killing the Lycans (Werewolves) who allegedly slaughtered her family.", 
	"https://upload.wikimedia.org/wikipedia/en/1/18/UnderworldFilmsCover.jpg", 
	"https://www.youtube.com/watch?v=MqT-e44kIM8")

vampire_academy = media.Movie("Vampire Academy", 
	"The story features seventeen-year-old Dhampir (half-human, half-vampire) guardian-in-training Rose Hathaway (Zoey Deutch), and her royal Moroi (the peaceful, mortal vampires) best friend Lissa Dragomir (Lucy Fry) living discreetly within our world, having escaped from their boarding school St. Vladimir's Academy one year prior to the beginning of the story, following a series of warnings and threats. They are soon dragged back to the Academy in Montana and rediscover the dangerous hierarchy within it, along with lies, rumors and secrets, both struggling to fit in to the school politics.", 
	"https://upload.wikimedia.org/wikipedia/en/e/e5/Vampire_Academy%2C_Blood_Sisters.jpeg", 
	"https://www.youtube.com/watch?v=D-_TxtG1CVw")

howls_moving_casle = media.Movie("Howl's Moving Castle", 
	"The film tells the story of a young hatter named Sophie after she is turned into an old woman by a witch's curse. She encounters a wizard named Howl, and gets caught up in his resistance to fighting for the king.", 
	"https://upload.wikimedia.org/wikipedia/en/a/a0/Howls-moving-castleposter.jpg", 
	"https://www.youtube.com/watch?v=iwROgK94zcM")

irobot = media.Movie("I, Robot", 
	"In 2035, humanoid robots serve humanity, and humans are protected from the robots by the Three Laws of Robotics.", 
	"https://upload.wikimedia.org/wikipedia/en/3/3b/Movie_poster_i_robot.jpg", 
	"https://www.youtube.com/watch?v=rL6RRIOZyCM")

ex_machina = media.Movie("Ex Machina", 
	"Computer programmer Caleb Smith wins a one-week visit to the luxurious, isolated home of Nathan Bateman, the CEO of his software company, Blue Book. The only other person there is Nathan's servant Kyoko, who Nathan says does not speak English. Nathan has built a humanoid robot named Ava with artificial intelligence (AI). Ava has already surpassed a simple Turing test; Nathan wants Caleb to judge whether Ava is genuinely capable of thought and consciousness, and whether he can relate to Ava despite knowing she is artificial.", 
	"https://images-na.ssl-images-amazon.com/images/I/41rsIeUZgbL._SX200_QL80_.jpg", 
	"https://www.youtube.com/watch?v=EoQuVnKhxaM")

my_movies = [event_horizon, ex_machina, vampire_academy, underworld, howls_moving_casle, irobot]
movies_from_class = [avatar, school_of_rock, ratatouille, hunger_games] # Toy Story and Mignight in Paris where removed due to content restriction
fresh_tomatoes.open_movies_page(my_movies + movies_from_class)

# print "Possible movie ratings: "
# print media.Movie.VALID_RATINGS
# print media.Movie.__doc__

