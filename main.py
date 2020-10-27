
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
import random

class MainScreen(BoxLayout):
	
	name_label = ObjectProperty(None)
	cost_label = ObjectProperty(None)
	q_label = ObjectProperty(None)
	planet_view = ObjectProperty(None)
	#earth_img = Image(source="earth.jpg")
	
	def say(self):
		planet_img =["teal_planet.png", "snow_planet.png", "bluered_planet.png", "green_planet.png", "white_planet.png", "desert_planet.png"]
		goods= [[planet_img[0], "gold", 250, 15], [planet_img[1], "iron", 102, 91], [planet_img[2], "chip", 199, 25], [planet_img[3], "weapon", 322, 3], [planet_img[4], "ration", 85, 410], [planet_img[5], "drugs", 760, 50]]
		g = random.choice(goods)
		self.planet_view.source = g[0]
		self.name_label.text = g[1]
		self.cost_label.text = str(g[2])
		self.q_label.text = str(g[3])


class StarMerchantApp(App):
		def build(self):
			return MainScreen()
			
		
		
if __name__ == "__main__":
	StarMerchantApp().run()