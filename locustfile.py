import logging
from test_data import TestData
from locust import HttpUser, task, events


@events.quitting.add_listener
def _(environment, **kw):
    if environment.stats.total.fail_ratio > 0.01:
        logging.error("Test failed due to failure ratio > 1%")
        environment.process_exit_code = 1
    elif environment.stats.total.avg_response_time > 200:
        logging.error("Test failed due to average response time ratio > 200 ms")
        environment.process_exit_code = 1
    elif environment.stats.total.get_response_time_percentile(0.95) > 800:
        logging.error("Test failed due to 95th percentile response time > 800 ms")
        environment.process_exit_code = 1
    else:
        environment.process_exit_code = 0


class MyUser(HttpUser):
    # wait_time = between(1, 3)

    def on_start(self):
        # This will be executed when a virtual user (Locust user) starts running.
        # Perform the login process here.
        self.client.cookies.set('L', 'hindi%2Cenglish%2Cpunjabi')
        self.client.cookies.set('geo', '0.0.0.0%2CIN%2CMaharashtra%2CNavi+Mumbai%2C400703')

    @task
    def check_emergency_services_001(self):
        response = self.client.get(
            '/api.php?__call=app.getLaunchData&app_version=9.7.2&ctx=android&api_version=4')
        assert response.status_code == 200

    @task
    def check_emergency_services_002(self):
        playlists_ids = TestData.playlist_ids
        for p in playlists_ids:
            path = f'/api.php?ctx=android&api_version=4&__call=playlist.getDetails&app_version=9.7.2&listid={p}'
            response = self.client.get(path, name="/api.php?ctx=android&api_version=4&__call=playlist.getDetails&app_version=9.7.2&listid=[p]")
            assert response.status_code == 200



    @task
    def check_emergency_services_003(self):
        album_ids = TestData.album_ids
        for a in album_ids:
            path = f'/api.php?ctx=android&api_version=4&app_version=9.7.2&__call=content.getAlbumDetails&albumid={a}'
            response = self.client.get(path, name= "'/api.php?ctx=android&api_version=4&app_version=9.7.2&__call=content.getAlbumDetails&albumid={a}")
            assert response.status_code == 200


    @task
    def check_emergency_service_004(self):
        song_ids = TestData.song_ids
        for s in song_ids:
            path = f'/api.php?&__call=song.getDetails&app_version=9.7.2&ctx=android&api_version=4&pids={s}'
            response = self.client.get(path, name= "/api.php?&__call=song.getDetails&app_version=9.7.2&ctx=android&api_version=4&pids={s}")
            assert response.status_code == 200


    @task
    def check_negative_scenario_005(self):
        # We will be accessing a show object
        show_data_1 = self.client.get(
                '/api.php?__call=show.getHomePage&show_id=394604&season_number=1&app_version=9.4.0&device_type'
                '=iPhone_XR&_format=json&ctx=iphoneapp&_marker=false&v=947&cc=in&network_type=WIFI&tz=asia/kolkata'
                '&network_subtype=WIFI&network_operator=jio&is_jio_user=false&api_version=4&season_number=1&show_id'
                '=394604')
        assert show_data_1.status_code == 404 or show_data_1.status_code == 500




