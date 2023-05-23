from test.test_setup import TestSetUp


# ==================== user registration ====================================

class UserRegistrationTest(TestSetUp):
    def test_if_all_the_input_fields_are_empty_user_should_return_error_message(self):
        response = self.client.post(self.register_url, data=self.invalid_data)
        self.assertEqual(response.status_code, 400)

    def test_if_any_one_of_the_input_fields_are_empty_user_should_not_get_registered(self):
        response = self.client.post(self.register_url, data=self.invalid_empty_field)
        self.assertEqual(response.status_code, 400)

    def test_user_should_get_registered_if_valid_input_is_given(self):  # success
        response = self.client.post(self.register_url, data=self.normal_user_data)
        self.assertEqual(response.status_code, 200)


# # ========================= user Login ========================================

class UserLoginTest(TestSetUp):
    def test_should_pass_if_username_and_password_are_valid(self):  # success
        self.client.post(self.register_url, data=self.normal_user_data)
        response = self.client.post(self.login_url, data=self.valid_login)
        self.assertEqual(response.status_code, 200)

    def test_if_username_and_password_are_empty_should_throw_error(self):
        self.client.post(self.register_url, data=self.normal_user_data)
        response = self.client.post(self.login_url, data=self.invalid_login_field)
        self.assertEqual(response.status_code, 400)

    def test_if_any_one_field_is_empty_should_throw_error(self):
        self.client.post(self.register_url, data=self.normal_user_data)
        response = self.client.post(self.login_url, data=self.empty_login_field)
        self.assertEqual(response.status_code, 400)

    def test_user_if_any_one_field_is_wrong_should_throw_error(self):
        self.client.post(self.register_url, data=self.normal_user_data)
        response = self.client.post(self.login_url, data=self.wrong_login)
        self.assertEqual(response.status_code, 400)



class BookTest(TestSetUp):
    """ test cases for book API"""

    def test_should_pass_if_valid_Book_details_are_added(self):
        token = self.get_admin_token()
        print(token)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        response = self.client.post(self.book_url, data=self.valid_book, format='json')
        self.assertEqual(response.status_code, 200)

    def test_should_fail_if_user_is_not_a_superuser(self):
        token = self.get_normal_user_token()
        print(token)
        book = {
            "book_name": "pqr",
            "description": "aaa",
            "author": "qqq",
            "price": 1020,
            "quantity": 2
        }
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        response = self.client.post(self.book_url, data=book, format='json')
        print(response.data.get("status"))
        self.assertEqual(response.data.get("status"), 400)


