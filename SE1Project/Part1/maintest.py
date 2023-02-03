from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.layout import Layout
from kivy.uix.widget import Widget
from kivy.config import Config

Config.set('graphics', 'fullscreen', 0)
Config.set('graphics', 'width', 568)
Config.set('graphics', 'height', 568)
Config.set('graphics', 'resizable', 0)
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty


class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)


class SubScreen(Screen):
    disasterName = StringProperty()
    description = StringProperty()
    howToPrepare = StringProperty()

    def __init__(self, **kwargs):
        super(SubScreen, self).__init__(**kwargs)
        self.disasterName = "aaa"
        self.description = "bbb"
        self.howToPrepare = "ccc"


class TestApp(App):
    def __init__(self, **kwargs):
        super(TestApp, self).__init__(**kwargs)
        self.title = 'DisasterList'

    def build(self):
        self.sm = ScreenManager()

        wildFires = SubScreen(name='wildFires')
        wildFires.disasterName = "Wildfires"
        wildFires.description = """Wildfires happen in areas with lots of dry vegetation, including forests and deserts with large amounts of brush. Natural causes like lightning and extreme drought can cause this California natural disaster, as well as human carelessness or bad intentions. Wildfires can very quickly burn large areas of wilderness and devastate neighborhoods and cities. In Southern California, especially, wildfires are frequent due to the warm climate and low rainfall."""
        wildFires.howToPrepare = """"Emergency Supply Kit Checklist
        1). Face masks or coverings
        2). Three-day supply of non-perishable food and three 
            gallons of water per person
        3). Map marked with at least two evacuation routes
        4). Prescriptions or special medications
        5). Change of clothing
        6). Extra eyeglasses or contact lenses
        7). An extra set of car keys, credit cards, 
            cash or traveler’s checks
        8). First aid kit
        9). Flashlight
        10). Battery-powered radio and extra batteries
        11). Sanitation supplies
        12). Copies of important documents (birth certificates, 
             passports, etc.)
        13). Don't forget pet food and water!
        """

        earthquakes = SubScreen(name='earthquakes')
        earthquakes.disasterName = "Earthquake"
        earthquakes.description = """California is highly prone to earthquakes as it sits on many active fault lines. Earthquakes are caused by sudden movements of the Earth’s crust along the fault lines. They are nearly impossible to predict.  The shock waves and ground movement can cause damage to structures, specially those that haven’t been built or reinforced to withstand an earthquake."""
        earthquakes.howToPrepare = """ 
        1). Create an earthquake safety plan for you and loved 
            ones, including pets.
        2). Identify safe places in each room of your home.
        3). Know your risk for earthquakes in your area and what 
            you must do to stay safe.
        4). Practice Drop, Cover, and Hold On with each member of 
            your household.
        5). Make or purchase earthquake safety kits.
        6). Find out if your home is in need of earthquake 
            retrofitting and eligible for a grant.
        7). Identify and fix potential earthquake hazards 
            in your home."""

        tsunamis = SubScreen(name='tsunamis')
        tsunamis.disasterName = 'Tsunamis'
        tsunamis.description = """a tsunami is a series of large, devastating waves that occur when a disturbance in the Earth quickly displaces large amounts of seawater. They can trigger earthquakes, landslides, meteorite impacts, or volcanic eruptions. Although they are a rare natural disaster, California is still susceptible to tsunamis due to the chance of an undersea earthquake near the coast."""
        tsunamis.howToPrepare = """Top Tips
        1). To escape a tsunami, go as high and as far as you can – 
            ideally to a spot 100 feet above sea level
            or 2 miles away.
        2). Every foot inland or upward may make a difference!
        3). If you can see the wave, you are too close for safety.

        Know the difference!

        1). A Tsunami WARNING means a tsunami may have been 
            generated and could be close to your area.
        2). A Tsunami WATCH means a tsunami has not yet been 
            verified but could exist and may be as little as 
            an hour away. 
            [Recommendation: Create unique infographic]"""

        floods = SubScreen(name='floods')
        floods.disasterName = 'Floods'
        floods.description = """Heavy rainfall often causes floods in California as well as other disasters like landslides and mudslides. These disasters do a considerable amount of damage to cars, homes, and other structures each year."""
        floods.howToPrepare = """ 
        1). Figure out their risk of flooding at home and 
            while traveling
        2). Learn what food and supplies are needed to shelter
            at home during a flood
        3). Determine what you should take with you if evacuating"""

        landSlides = SubScreen(name='landslides')
        landSlides.disasterName = 'Landslides and Mudslides'
        landSlides.description = """Landslides occur in hilly or mountainous areas when soil, rocks, vegetation, and other debris begin moving downhill rapidly. Earthquakes can cause them,as can an existing instability in the land. Mudslides, a form of landslide, happen when heavy rainfall causes loose mud and soil to slide downhill. In California, these natural disasters occur regularly in areas that experience earthquakes and periods of heavy rain."""
        landSlides.howToPrepare = """
        1). Become familiar with the land around your home and 
            work to understand your risk in different situations
        2). Watch the patterns of storm water drainage on slopes 
            near your home and work, especially where runoff 
            water converges
        3). Learn about local emergence response 
            and evacuation plans
        4). Create and practice an evacuation plan for everyone in 
            your family and your business
        5).Assemble and maintain an emergency preparedness kit"""

        self.sm.add_widget(MainScreen(name='main'))
        self.sm.add_widget(wildFires)
        self.sm.add_widget(earthquakes)
        self.sm.add_widget(tsunamis)
        self.sm.add_widget(floods)
        self.sm.add_widget(landSlides)
        return self.sm


if __name__ == '__main__':
    TestApp().run()


