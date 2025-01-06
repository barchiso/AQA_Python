"""Homework #25. Work with locators."""
# 1. Write 25 XPath and 25 CSS locators
# for the site https://qauto2.forstudy.space/
# 2. Use the text () function, search by attribute @ ,
# and complex locators (more than one element)
# 3. Data for login to the site -
# login - guest
# pass - welcome2qauto

import pytest
from playwright.sync_api import expect, sync_playwright

BASE_URL = 'https://guest:welcome2qauto@qauto2.forstudy.space/'


class TestQauto:
    """Test class for interacting with the QAuto website using Playwright."""

    @pytest.fixture(scope='class')
    def main_page(self):
        """Fixture to set up Playwright browser and page for each test.

        Yields:
            page: The Playwright page object for interacting with the webpage.
        """
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=False)
            context = browser.new_context()
            page = context.new_page()
            page.goto(BASE_URL)
            yield page
            context.close()
            browser.close()

    def test_page_headers(self, main_page):
        """Test to check header elements on the page.

        Args:
            main_page: The Playwright page object to interact with the webpage.
        """
        # Display logo.
        logo_selector = main_page.locator('.header_logo')  # CSS locator # 1
        expect(logo_selector).to_be_visible()
        # Check for the presence of an <svg> element within .header_logo
        svg_selector = logo_selector.locator('svg')  # CSS locator # 2
        expect(svg_selector).to_be_visible()
        # Verify the xmlns attribute in the <svg> element
        expect(svg_selector).to_have_attribute(
            'xmlns', 'http://www.w3.org/2000/svg')

        # Display navigation buttons.
        navigation_buttons = main_page.locator(
            '.header_nav ')  # CSS locator # 3
        expect(navigation_buttons).to_be_visible()

        home_button_locator = main_page.locator(
            '//a[text()="Home"]')  # XPath locator # 1
        expect(home_button_locator).to_be_visible()
        expect(home_button_locator).to_have_text('Home')

        about_button_locator = main_page.locator(
            '//button[text() = "About"]')  # XPath locator # 2
        expect(about_button_locator).to_be_visible()
        expect(about_button_locator).to_have_text('About')

        contacts_button_locator = main_page.locator(
            '//button[text()="Contacts"]')  # XPath locator # 3
        expect(contacts_button_locator).to_be_visible()
        expect(contacts_button_locator).to_have_text('Contacts')

        guest_button_locator = main_page.locator(
            '//button[text()="Guest log in"]')  # XPath locator # 4
        expect(guest_button_locator).to_be_visible()
        expect(guest_button_locator).to_have_text('Guest log in')

        signin_button_locator = main_page.locator(
            '//button[text()="Sign In"]')  # XPath locator # 5
        expect(signin_button_locator).to_be_visible()
        expect(signin_button_locator).to_have_text('Sign In')

    def test_page_hero_section(self, main_page):
        """Test to check the hero section's visibility and content.

        Args:
            main_page: The Playwright page object to interact with the webpage.
        """
        section_title_locator = main_page.locator(
            '//h1[text()="Do more!"]')  # XPath locator # 6
        expect(section_title_locator).to_be_visible()
        expect(section_title_locator).to_have_text('Do more!')

        section_description_locator = main_page.locator(
            '.hero-descriptor_descr.lead')  # CSS locator # 4
        expect(section_description_locator).to_be_visible()
        expect(section_description_locator).to_have_text(
            'With the help of the Hillel auto project, you will have the '
            'opportunity to get hands-on experience in manual testing.')

        signup_button_locator = main_page.locator(
            '//button[text()="Sign up"]')  # XPath locator # 7
        expect(signup_button_locator).to_be_visible()
        expect(signup_button_locator).to_have_text('Sign up')

        section_video_locator = main_page.locator(
            '.hero-video_frame')  # CSS locator # 5
        expect(section_video_locator).to_be_visible()
        expect(section_video_locator).to_have_attribute(
            'src',
            'https://www.youtube.com/embed/znjjC0Iw8Wc?showinfo=0&controls=0')

    def test_page_about_section(self, main_page):
        """Test to check elements in the 'About' section.

        Args:
            main_page: The Playwright page object to interact with the webpage.
        """
        fuel_expenses_image_locator = main_page.locator(
            'img[src="/assets/images/homepage/info_1.jpg"]')  # CSS locator # 6
        expect(fuel_expenses_image_locator).to_be_visible()
        expect(fuel_expenses_image_locator).to_have_attribute(
            'src',
            '/assets/images/homepage/info_1.jpg')

        instructions_image_locator = main_page.locator(
            'img[src="/assets/images/homepage/info_2.jpg"]')  # CSS locator # 7
        expect(instructions_image_locator).to_be_visible()
        expect(instructions_image_locator).to_have_attribute(
            'src',
            '/assets/images/homepage/info_2.jpg')

        fuel_expenses_title_locator = main_page.locator(
            '//p[text()="Log fuel expenses"]')  # XPath locator # 8
        expect(fuel_expenses_title_locator).to_be_visible()
        expect(fuel_expenses_title_locator).to_have_text(
            'Log fuel expenses')

        fuel_expenses_text_locator = main_page.locator(
            # XPath locator # 9
            '//p[contains(text(),"Keep track of your replacement schedule")]')
        expect(fuel_expenses_text_locator).to_be_visible()
        expect(fuel_expenses_text_locator).to_have_text(
            'Keep track of your replacement schedule and plan your vehicle'
            ' maintenance expenses in advance.')

        instructions_title_locator = main_page.locator(
            '//p[text()="Instructions and manuals"]')  # XPath locator # 10
        expect(instructions_title_locator).to_be_visible()
        expect(instructions_title_locator).to_have_text(
            'Instructions and manuals')

        instructions_text_locator = main_page.locator(
            # XPath locator # 11
            '//p[contains(text(),"Watch over 100 instructions and repair")]')
        expect(instructions_text_locator).to_be_visible()
        expect(instructions_text_locator).to_have_text(
            'Watch over 100 instructions and repair your car yourself.')

    def test_page_contacts_section(self, main_page):
        """Test to check elements in the 'Contacts' section.

        Args:
            main_page: The Playwright page object to interact with the webpage.
        """
        contacts_title_locator = main_page.locator(
            '//h2[text()="Contacts"]')  # XPath locator # 12
        expect(contacts_title_locator).to_be_visible()
        expect(contacts_title_locator).to_have_text('Contacts')

        facebook_icon_locator = main_page.locator(
            '.icon-facebook')  # CSS locator # 8
        facebook_link_locator = facebook_icon_locator.locator('..')
        expect(facebook_icon_locator).to_be_visible()
        expect(facebook_link_locator).to_have_attribute(
            'href',
            'https://www.facebook.com/Hillel.IT.School')

        telegram_icon_locator = main_page.locator(
            '.icon-telegram')  # CSS locator # 9
        telegram_link_locator = telegram_icon_locator.locator('..')
        expect(telegram_icon_locator).to_be_visible()
        expect(telegram_link_locator).to_have_attribute(
            'href',
            'https://t.me/ithillel_kyiv')

        youtube_icon_locator = main_page.locator(
            '.icon-youtube')  # CSS locator # 10
        youtube_link_locator = youtube_icon_locator.locator('..')
        expect(youtube_icon_locator).to_be_visible()
        expect(youtube_link_locator).to_have_attribute(
            'href',
            'https://www.youtube.com/user/HillelITSchool?sub_confirmation=1')

        instagram_icon_locator = main_page.locator(
            '.icon-instagram')  # CSS locator # 11
        instagram_link_locator = instagram_icon_locator.locator('..')
        expect(instagram_icon_locator).to_be_visible()
        expect(instagram_link_locator).to_have_attribute(
            'href',
            'https://www.instagram.com/hillel_itschool/')

        linkedin_icon_locator = main_page.locator(
            '.icon-linkedin')  # CSS locator # 12
        linkedin_link_locator = linkedin_icon_locator.locator('..')
        expect(linkedin_icon_locator).to_be_visible()
        expect(linkedin_link_locator).to_have_attribute(
            'href',
            'https://www.linkedin.com/school/ithillel/')

        site_icon_locator = main_page.locator(
            '//a[text()="ithillel.ua"]')  # XPath locator # 13
        expect(site_icon_locator).to_be_visible()
        expect(site_icon_locator).to_have_text(
            'ithillel.ua')
        expect(site_icon_locator).to_have_attribute(
            'href',
            'https://ithillel.ua')

        email_icon_locator = main_page.locator(
            '.contacts_link.h4')  # CSS locator # 13
        expect(email_icon_locator).to_be_visible()
        expect(email_icon_locator).to_have_text(
            'support@ithillel.ua')
        expect(email_icon_locator).to_have_attribute(
            'href',
            'mailto:developer@ithillel.ua')

    def test_page_footer_section(self, main_page):
        """Test to check visibility and content of footer section.

        Args:
            main_page: The Playwright page object to interact with the webpage.
        """
        copyright_text_locator = main_page.locator(
            '//p[text()="© 2021 Hillel IT school"]')  # XPath locator # 14
        expect(copyright_text_locator).to_be_visible()
        expect(copyright_text_locator).to_have_text(
            '© 2021 Hillel IT school')

        footer_description_locator = main_page.locator(
            # XPath locator # 15
            '//p[contains(text(), "Hillel auto developed in Hillel IT")]')
        expect(footer_description_locator).to_be_visible()
        expect(footer_description_locator).to_have_text(
            'Hillel auto developed in Hillel IT school '
            'for educational purposes of QA courses.')

        # Display logo.
        footer_logo = main_page.locator('.footer_logo')  # CSS locator # 14
        expect(footer_logo).to_be_visible()
        # Check for the presence of an <svg> element within .header_logo
        footer_svg = footer_logo.locator('svg')  # CSS locator # 15
        expect(footer_svg).to_be_visible()
        # Verify the xmlns attribute in the <svg> element
        expect(footer_svg).to_have_attribute(
            'xmlns', 'http://www.w3.org/2000/svg')

    def test_page_registration_modal(self, main_page):
        """Test to check elements on the Sign Up modal window.

        Args:
            main_page: The Playwright page object to interact with the webpage.
        """
        # Open Sign Up modal window.
        main_page.locator('//button[text() = "Sign up"]').click()
        signup_modal = main_page.locator(
            '.modal-content')  # CSS locator # 16
        expect(signup_modal).to_be_visible()

        signup_title_locator = main_page.locator(
            '.modal-title')   # CSS locator # 17
        expect(signup_title_locator).to_be_visible()
        expect(signup_title_locator).to_have_text(
            'Registration')

        signup_name_field_title = main_page.locator(
            '//label[text()="Name"]')    # XPath locator # 16
        expect(signup_name_field_title).to_be_visible()
        expect(signup_name_field_title).to_have_text(
            'Name')

        signup_name_field = main_page.locator(
            '#signupName')   # CSS locator # 18
        expect(signup_name_field).to_be_visible()
        signup_name_field.focus()
        signup_name_field.blur()
        expect(signup_name_field).to_have_css(
            'border-color', 'rgb(220, 53, 69)')

        signup_name_field_error = main_page.locator(
            '//p[text()="Name required"]')    # XPath locator # 17
        expect(signup_name_field_error).to_be_visible()
        expect(signup_name_field_error).to_have_text(
            'Name required')
        expect(signup_name_field_error).to_have_css(
            'border-color', 'rgb(220, 53, 69)')

        signup_lastname_field_title = main_page.locator(
            '//label[text()="Last name"]')    # XPath locator # 18
        expect(signup_lastname_field_title).to_be_visible()
        expect(signup_lastname_field_title).to_have_text(
            'Last name')

        signup_lastname_field = main_page.locator(
            '#signupLastName')   # CSS locator # 19
        expect(signup_lastname_field).to_be_visible()
        signup_lastname_field.focus()
        signup_lastname_field.blur()
        expect(signup_lastname_field).to_have_css(
            'border-color', 'rgb(220, 53, 69)')

        signup_lastname_field_error = main_page.locator(
            '//p[text()="Last name required"]')    # XPath locator # 19
        expect(signup_lastname_field_error).to_be_visible()
        expect(signup_lastname_field_error).to_have_text(
            'Last name required')
        expect(signup_lastname_field_error).to_have_css(
            'border-color', 'rgb(220, 53, 69)')

        signup_email_field_title = main_page.locator(
            '//label[text()="Email"]')    # XPath locator # 20
        expect(signup_email_field_title).to_be_visible()
        expect(signup_email_field_title).to_have_text(
            'Email')

        signup_email_field = main_page.locator(
            '#signupEmail')   # CSS locator # 20
        expect(signup_email_field).to_be_visible()
        signup_email_field.focus()
        signup_email_field.blur()
        expect(signup_email_field).to_have_css(
            'border-color', 'rgb(220, 53, 69)')

        signup_email_field_error = main_page.locator(
            '//p[text()="Email required"]')    # XPath locator # 21
        expect(signup_email_field_error).to_be_visible()
        expect(signup_email_field_error).to_have_text(
            'Email required')
        expect(signup_email_field_error).to_have_css(
            'border-color', 'rgb(220, 53, 69)')

        signup_password_field_title = main_page.locator(
            '//label[text()="Password"]')    # XPath locator # 22
        expect(signup_password_field_title).to_be_visible()
        expect(signup_password_field_title).to_have_text(
            'Password')

        signup_password_field = main_page.locator(
            '#signupPassword')   # CSS locator # 21
        expect(signup_password_field).to_be_visible()
        signup_password_field.focus()
        signup_password_field.blur()
        expect(signup_password_field).to_have_css(
            'border-color', 'rgb(220, 53, 69)')

        signup_password_field_error = main_page.locator(
            '//p[text()="Password required"]')    # XPath locator # 23
        expect(signup_password_field_error).to_be_visible()
        expect(signup_password_field_error).to_have_text(
            'Password required')
        expect(signup_password_field_error).to_have_css(
            'border-color', 'rgb(220, 53, 69)')

        reenter_password_field_title = main_page.locator(
            '//label[text()="Re-enter password"]')    # XPath locator # 24
        expect(reenter_password_field_title).to_be_visible()
        expect(reenter_password_field_title).to_have_text(
            'Re-enter password')

        reenter_password_field = main_page.locator(
            '#signupRepeatPassword')   # CSS locator # 22
        expect(reenter_password_field).to_be_visible()
        reenter_password_field.focus()
        reenter_password_field.blur()
        expect(reenter_password_field).to_have_css(
            'border-color', 'rgb(220, 53, 69)')

        reenter_password_field_error = main_page.locator(
            '//p[text()="Re-enter password required"]')    # XPath locator # 25
        expect(reenter_password_field_error).to_be_visible()
        expect(reenter_password_field_error).to_have_text(
            'Re-enter password required')
        expect(reenter_password_field_error).to_have_css(
            'border-color', 'rgb(220, 53, 69)')

        signup_button = main_page.locator(
            'button[class="btn btn-primary"]')  # CSS locator # 23
        expect(signup_button).to_be_visible()
        expect(signup_button).to_have_text(
            'Register')
        expect(signup_button).to_have_attribute('disabled', '')

        signup_close_button = main_page.locator(
            'span[aria-hidden="true"]')  # CSS locator # 24
        expect(signup_close_button).to_be_visible()
        expect(signup_close_button).to_have_text('×')
        signup_close_button.click()
        expect(signup_modal).not_to_be_visible()

    def test_page_login_modal(self, main_page):
        """Test to check elements on the Log in modal window.

        Args:
            main_page: The Playwright page object to interact with the webpage.
        """
        # Open Log in modal window.
        main_page.locator('//button[text() = "Sign In"]').click()
        login_modal = main_page.locator(
            '.modal-content')
        expect(login_modal).to_be_visible()

        login_title = main_page.locator(
            '.modal-title')
        expect(login_title).to_be_visible()
        expect(login_title).to_have_text(
            'Log in')

        login_email_field_title = main_page.locator(
            '//label[text()="Email"]')
        expect(login_email_field_title).to_be_visible()
        expect(login_email_field_title).to_have_text(
            'Email')

        login_email_field = main_page.locator(
            '#signinEmail')   # CSS locator # 25
        expect(login_email_field).to_be_visible()
        login_email_field.focus()
        login_email_field.blur()
        expect(login_email_field).to_have_css(
            'border-color', 'rgb(220, 53, 69)')

        login_email_field_error = main_page.locator(
            '//p[text()="Email required"]')
        expect(login_email_field_error).to_be_visible()
        expect(login_email_field_error).to_have_text(
            'Email required')
        expect(login_email_field_error).to_have_css(
            'border-color', 'rgb(220, 53, 69)')

        login_password_field_title = main_page.locator(
            '//label[text()="Password"]')
        expect(login_password_field_title).to_be_visible()
        expect(login_password_field_title).to_have_text(
            'Password')

        login_password_field = main_page.locator(
            '#signinPassword')   # CSS locator # 26
        expect(login_password_field).to_be_visible()
        login_password_field.focus()
        login_password_field.blur()
        expect(login_password_field).to_have_css(
            'border-color', 'rgb(220, 53, 69)')

        login_password_field_error = main_page.locator(
            '//p[text()="Password required"]')
        expect(login_password_field_error).to_be_visible()
        expect(login_password_field_error).to_have_text(
            'Password required')
        expect(login_password_field_error).to_have_css(
            'border-color', 'rgb(220, 53, 69)')

        login_registration_button = main_page.locator(
            '//button[text()="Registration"]')    # XPath locator # 26
        expect(login_registration_button).to_be_visible()
        expect(login_registration_button).to_have_text(
            'Registration')

        login_remember = main_page.locator(
            '[for="remember"]')  # CSS locator # 27
        expect(login_remember).to_be_visible()
        expect(login_remember).to_have_text(
            'Remember me')

        login_remember_checkbox = main_page.locator(
            '#remember')  # CSS locator # 28
        expect(login_remember_checkbox).to_be_visible()
        expect(login_remember_checkbox).not_to_be_checked()
        login_remember_checkbox.click()
        expect(login_remember_checkbox).to_be_checked()
        login_remember_checkbox.click()
        expect(login_remember_checkbox).not_to_be_checked()

        forgot_password_button = main_page.locator(
            '//button[text()="Forgot password"]')   # XPath locator # 27
        expect(forgot_password_button).to_be_visible()
        expect(forgot_password_button).to_have_text(
            'Forgot password')

        login_button = main_page.locator(
            'button[class="btn btn-primary"]')
        expect(login_button).to_be_visible()
        expect(login_button).to_have_text(
            'Login')
        expect(login_button).to_have_attribute('disabled', '')

        login_close_button = main_page.locator(
            'button[aria-label="Close"]')  # CSS locator # 29
        expect(login_close_button).to_be_visible()
        expect(login_close_button).to_have_text('×')
        login_close_button.click()
        expect(login_modal).not_to_be_visible()
