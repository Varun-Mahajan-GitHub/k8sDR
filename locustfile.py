import random
import string
import time
from asyncio import events

from allure_pytest.listener import AllureListener
from locust import HttpUser, task, between
import allure


@allure.feature("ios_performance_testing")
class MyUser(HttpUser):
    wait_time = between(1, 3)

    def on_start(self):
        # This will be executed when a virtual user (Locust user) starts running.
        # Perform the login process here.
        self.login()

    def login(self):
        # Define the login request to the backend API.
        characters = string.ascii_lowercase + string.digits + '_-'
        username = ''.join(random.choice(characters) for _ in range(10))
        domain = 'saavn.com'
        email = f"{username}@{domain}"
        password = 'Saavn123'
        login_payload = {
            "username": email,
            "password": password
        }
        response = self.client.post("/api.php?__call=user.login&api_version=4&_format=json&_marker=0&ctx=iphoneapp",
                                    json=login_payload)

        # Check if the login was successful (use appropriate HTTP status code or response data).
        if response.status_code == 200:
            print("Login successful!")
        else:
            print("Login failed!")

    @task
    @allure.story("create_playlist_and_add_content_to_it")
    def create_playlist_and_add_content_to_it(self):
        # This is an example of another task that requires authentication.
        playlist = str(time.time())
        print(f'the name of the playlist is {playlist}')
        response = self.client.post(
            '/api.php?__call=playlist.create&share=true&contents=~~pQHQxGEl~&listname=%s&app_version=9.4.0&device_type=iPhone_XR&_format=json&ctx=iphoneapp&_marker=false&v=947&cc=in&network_type=WIFI&tz=asia/kolkata&network_subtype=WIFI&network_operator=jio&is_jio_user=false&api_version=4' % playlist)

        if response.status_code == 200:
            print('playlist creation successful')
        else:
            print('Playlist creation failed')

        data = response.json()
        list_id = data['details']['id']
        print(f'The id of the new list created is {list_id}')
        playlistdetails = self.client.post(
            '/api.php?__call=playlist.getDetails&modules=false&listid=%s&app_version=9.4.0&device_type=iPhone_XR&_format=json&ctx=iphoneapp&_marker=false&v=947&cc=in&network_type=WIFI&network_subtype=WIFI&network_operator=jio&tz=asia/kolkata&dolby_support=true&is_jio_user=false&api_version=4' % list_id)
        playlist_save_1 = self.client.post(
            'api.php?__call=playlist.save&contents=~~pQHQxGEl~%5E~~T1QDhzdZ~%5E~~qZtKBMZ_~%5E~~IhKbmgyP~%5E~~BuuUaa07~%5E~~cnIjWjPB~%5E~~co1pPKYl~%5E~~DY931hLE~%5E~~XPQbUeGB~%5E~~xCqNWWqG~%5E~~Jxu4-xQ8~%5E~~SNkDIrfg~%5E~~gOgEpIdd~%5E~~rxMX-VHq~%5E~~BAiADMge~%5E~~8DMj37qS~%5E~~IrEzzCfb~%5E~~B-gQZSJo~%5E~~EbFWakDs~%5E~~1glW_JN3~%5E~~i045UaSh~%5E~~1eGJGc20~%5E~~LP3-QFBE~%5E~~msoqdqua~%5E~~o59Ryw-L~%5E~~UMYBB5nW~&listid=' + list_id + '&app_version=9.4.0&device_type=iPhone_XR&_format=json&ctx=iphoneapp&_marker=false&v=947&cc=in&network_type=WIFI&tz=asia/kolkata&network_subtype=WIFI&network_operator=jio&is_jio_user=false&api_version=4')
        playlist_save_2 = self.client.post((
                '/api.php?__call=playlist.save&contents=~~pQHQxGEl~%5E~~T1QDhzdZ~%5E~~qZtKBMZ_~%5E~~IhKbmgyP~%5E~~BuuUaa07~%5E~~cnIjWjPB~%5E~~co1pPKYl~%5E~~DY931hLE~%5E~~XPQbUeGB~%5E~~xCqNWWqG~%5E~~Jxu4-xQ8~%5E~~SNkDIrfg~%5E~~gOgEpIdd~%5E~~rxMX-VHq~%5E~~BAiADMge~%5E~~8DMj37qS~%5E~~IrEzzCfb~%5E~~B-gQZSJo~%5E~~EbFWakDs~%5E~~1glW_JN3~%5E~~i045UaSh~%5E~~1eGJGc20~%5E~~LP3-QFBE~%5E~~msoqdqua~%5E~~o59Ryw-L~%5E~~UMYBB5nW~&listid=' + list_id + '&app_version=9.4.0&device_type=iPhone_XR&_format=json&ctx=iphoneapp&_marker=false&v=947&cc=in&network_type=WIFI&tz=asia/kolkata&network_subtype=WIFI&network_operator=jio&is_jio_user=false&api_version=4'))
        playlist_save_3 = self.client.post((
                '/api.php?__call=playlist.save&listid=' + list_id + '&contents=~~pQHQxGEl~%5E~~T1QDhzdZ~%5E~~qZtKBMZ_~%5E~~IhKbmgyP~%5E~~BuuUaa07~%5E~~cnIjWjPB~%5E~~co1pPKYl~%5E~~DY931hLE~%5E~~XPQbUeGB~%5E~~xCqNWWqG~%5E~~Jxu4-xQ8~%5E~~SNkDIrfg~%5E~~gOgEpIdd~%5E~~rxMX-VHq~%5E~~BAiADMge~%5E~~8DMj37qS~%5E~~IrEzzCfb~%5E~~B-gQZSJo~%5E~~EbFWakDs~%5E~~1glW_JN3~%5E~~i045UaSh~%5E~~1eGJGc20~%5E~~LP3-QFBE~%5E~~msoqdqua~%5E~~o59Ryw-L~%5E~~UMYBB5nW~%5E~~hG9gnvNF~%5E~~-fZxHyJp~%5E~~uiEWT3kP~%5E~~TJh8tz7R~%5E~~2XLkr2Gd~%5E~~iQvnfPnq~%5E~~3Be_U0qz~%5E~~cymtugLP~%5E~~tdhrN_9I~%5E~~gmu8r1rk~%5E~~nHE_hXAv~%5E~~UOva6sV5~%5E~~mTYK5ypj~%5E~~5JEiviDK~%5E~~oDUdM0Sh~%5E~~J8CQvXyt~%5E~~br6P4rkk~%5E~~Q_3-2YCw~%5E~~DBJ5G8Od~%5E~~n9tYLmzr~&app_version=9.4.0&device_type=iPhone_XR&_format=json&ctx=iphoneapp&_marker=false&v=947&cc=in&network_type=WIFI&tz=asia/kolkata&network_subtype=WIFI&network_operator=jio&is_jio_user=false&api_version=4'))
        playlist_save_4 = self.client.post((
                                                       '/api.php?__call=playlist.save&listid=' + list_id + '&contents=~~pQHQxGEl~%5E~~T1QDhzdZ~%5E~~qZtKBMZ_~%5E~~IhKbmgyP~%5E~~BuuUaa07~%5E~~cnIjWjPB~%5E~~co1pPKYl~%5E~~DY931hLE~%5E~~XPQbUeGB~%5E~~xCqNWWqG~%5E~~Jxu4-xQ8~%5E~~SNkDIrfg~%5E~~gOgEpIdd~%5E~~rxMX-VHq~%5E~~BAiADMge~%5E~~8DMj37qS~%5E~~IrEzzCfb~%5E~~B-gQZSJo~%5E~~EbFWakDs~%5E~~1glW_JN3~%5E~~i045UaSh~%5E~~1eGJGc20~%5E~~LP3-QFBE~%5E~~msoqdqua~%5E~~o59Ryw-L~%5E~~UMYBB5nW~%5E~~hG9gnvNF~%5E~~-fZxHyJp~%5E~~uiEWT3kP~%5E~~TJh8tz7R~%5E~~2XLkr2Gd~%5E~~iQvnfPnq~%5E~~3Be_U0qz~%5E~~cymtugLP~%5E~~tdhrN_9I~%5E~~gmu8r1rk~%5E~~nHE_hXAv~%5E~~UOva6sV5~%5E~~mTYK5ypj~%5E~~5JEiviDK~%5E~~oDUdM0Sh~%5E~~J8CQvXyt~%5E~~br6P4rkk~%5E~~Q_3-2YCw~%5E~~DBJ5G8Od~%5E~~n9tYLmzr~%5E~~slBkC5rW~%5E~~j-pp3zq4~%5E~~ZbKc-WOt~%5E~~vFKmHXAx~%5E~~62JpyoRX~%5E~~mjqz9-9T~%5E~~ZvA9-sEw~%5E~~x6AUtNJO~%5E~~tn6UawO8~%5E~~rEk2hsSm~%5E~~HbsFJnrw~%5E~~tc_QX8gX~%5E~~gIp75iXe~%5E~~7w35MmsQ~%5E~~mCIGkpQF~%5E~~TTVK-qak~%5E~~EJS3aZ5B~%5E~~q-9UFKCv~%5E~~plBYp8Lj~%5E~~6GMaMFTj~%5E~~KLCgX51T~&app_version=9.4.0&device_type=iPhone_XR&_format=json&ctx=iphoneapp&_marker=false&v=947&cc=in&network_type=WIFI&tz=asia/kolkata&network_subtype=WIFI&network_operator=jio&is_jio_user=false&api_version=4'))

    @task
    @allure.story("open_podcast_home")
    def open_podcast_home(self):
        podcast_get_all = self.client.get(
            '/api.php?__call=podcast.getAll&app_version=9.4.0&device_type=iPhone_XR&_format=json&ctx=iphoneapp&_marker=false&v=947&cc=in&network_type=WIFI&network_subtype=WIFI&network_operator=jio&tz=asia/kolkata&dolby_support=true&is_jio_user=false&api_version=4')
        data = podcast_get_all.json()
        show_data_1 = self.client.get(
            '/api.php?__call=show.getHomePage&show_id=394604&season_number=1&app_version=9.4.0&device_type=iPhone_XR&_format=json&ctx=iphoneapp&_marker=false&v=947&cc=in&network_type=WIFI&tz=asia/kolkata&network_subtype=WIFI&network_operator=jio&is_jio_user=false&api_version=4&season_number=1&show_id=394604')
        show_data_2 = self.client.get(
            '/api.php?__call=show.getHomePage&season_number=3&show_id=71214&app_version=9.4.0&device_type=iPhone_XR&_format=json&ctx=iphoneapp&_marker=false&v=947&cc=in&network_type=WIFI&tz=asia/kolkata&network_subtype=WIFI&network_operator=jio&is_jio_user=false&api_version=4&season_number=3&show_id=71214')
        print(data)

    @task
    @allure.story("check_app_launch")
    def check_app_launch(self):
        library_data = self.client.get(
            '/api.php?__call=library.getAll&move_artist_pref=false&app_version=9.4.0&device_type=iPhone_XR&_format=json&ctx=iphoneapp&_marker=false&v=947&cc=in&network_type=WIFI&network_subtype=WIFI&network_operator=jio&tz=asia/kolkata&dolby_support=true&is_jio_user=false&api_version=4')
        content_data = self.client.get(
            '/api.php?__call=content.getBrowseModules&app_version=9.4.0&device_type=iPhone_XR&_format=json&ctx=iphoneapp&_marker=false&v=947&cc=in&network_type=WIFI&tz=asia/kolkata&network_subtype=WIFI&network_operator=jio&is_jio_user=false&api_version=4')
        homepage_data_v2 = self.client.get(
            '/api.php?__call=content.getHomepageDataV2&type=all&app_version=9.4.0&device_type=iPhone_XR&_format=json&ctx=iphoneapp&_marker=false&v=947&cc=in&tz=asia/kolkata&network_operator=jio&is_jio_user=false&api_version=4&type=all')
        app_launch_data = self.client.get(
            '/api.php?__call=content.getBrowseModules&app_version=9.4.0&device_type=iPhone_XR&_format=json&ctx=iphoneapp&_marker=false&v=947&cc=in&network_type=WIFI&tz=asia/kolkata&network_subtype=WIFI&network_operator=jio&is_jio_user=false&api_version=4')
        product_v2response = self.client.get(
            '/api.php?__call=products.listv2&auto_renewal=1&product_name=free&vendor=&status=free&country_code=IND&app_version=9.4.0&device_type=iPhone_XR&_format=json&ctx=iphoneapp&_marker=false&v=947&cc=in&network_type=WIFI&network_subtype=WIFI&network_operator=jio&tz=asia/kolkata&dolby_support=true&is_jio_user=false&api_version=4')

    @task
    @allure.story("start_radio")
    def start_radio(self):
        stationId = self.client.get(
            '/api.php?__call=webradio.createTagStation&language=hindi&tags=%7B%22topics%22:%5B%22hindicluster_6264%22%5D%7D&explicit=1&type=genre&mode=discover&t=712862161.954570&app_version=9.4.0&device_type=iPhone_XR&_format=json&ctx=iphoneapp&_marker=false&v=947&cc=in&network_type=WIFI&network_subtype=WIFI&network_operator=jio&tz=asia/kolkata&dolby_support=true&is_jio_user=false&api_version=4')
        songs = self.client.get(
            '/api.php?__call=webradio.getSong&k=20&stationid=8HgouMHQsWbA,w97p-EFlmLcTdG18b5HSmfC2t4ce9IPXSdEsbupVQ__&type=scratch&t=712862162.709143&app_version=9.4.0&device_type=iPhone_XR&_format=json&ctx=iphoneapp&_marker=false&v=947&cc=in&network_type=WIFI&tz=asia/kolkata&network_subtype=WIFI&network_operator=jio&is_jio_user=false&api_version=4&k=20&stationid=8HgouMHQsWbA%2Cw97p-EFlmLcTdG18b5HSmfC2t4ce9IPXSdEsbupVQ__&t=712862162.709143&type=scratch')
        next_song = self.client.get(
            '/api.php?__call=webradio.getSong&type=scratch&next=1&t=712862164.279300&songid=gTOlL2wh&stationid=8HgouMHQsWbA,w97p-EFlmLcTdG18b5HSmfC2t4ce9IPXSdEsbupVQ__&playtime=288&progress=0&k=1&app_version=9.4.0&device_type=iPhone_XR&_format=json&ctx=iphoneapp&_marker=false&v=947&cc=in&network_type=WIFI&tz=asia/kolkata&network_subtype=WIFI&network_operator=jio&is_jio_user=false&api_version=4&k=1&next=1&playtime=288&progress=0&songid=gTOlL2wh&stationid=8HgouMHQsWbA%2Cw97p-EFlmLcTdG18b5HSmfC2t4ce9IPXSdEsbupVQ__&t=712862164.279300&type=scratch')

    @task
    @allure.story("library")
    def library(self):
        response = self.client.get(
            '/api.php?__call=library.getAll&move_artist_pref=false&app_version=9.4.0&device_type=iPhone_XR&_format=json&ctx=iphoneapp&_marker=false&v=947&cc=in&network_type=WIFI&network_subtype=WIFI&network_operator=jio&tz=asia/kolkata&dolby_support=true&is_jio_user=false&api_version=4')


# Add the Allure listener to the Locust environment
events.request_success.add_listener(AllureListener())
events.request_failure.add_listener(AllureListener())
events.quitting.add_listener(write_artifacts)