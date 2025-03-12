# Testing documentation

[Manual Testing](#manual-testing)

[Automated Testing](#automated-testing)

- [Django Unit Tests](#django-unit-tests)
- [HTML Validation Tests](#html-validation-tests)
- [CSS Validation Tests](#css-validation-tests)
- [Javascript Validation Tests](#javascript-validation-tests)
- [Python Validation Tests](#python-validation-tests)
- [Lighthouse Scores](#lighthouse-scores)
- [Browser Compatibility](#browser-compatibility)
- [Accessibility](#Accessibility)
- [Responsiveness](#Responsiveness)

## Manual Testing

| **Feature**                     | **Expectation**                                                                                                                                | **Test**                                                                                                                           | **Result** |
| ------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| **Sign-up feature**             | Users should be able to create an account by entering an email, username, and password. Errors should be displayed for taken usernames/emails. | Attempt to sign up with unique and duplicate credentials. Check if appropriate error messages appear.                              | ✅         |
| **Sign-in feature**             | Users should be able to log in using valid credentials and authentication should fail for invalid credentials.                                 | Attempt to log in with correct and incorrect credentials.                                                                          | ✅         |
| **View posts**                  | Users should be able to see a list of posts, including author, content, and timestamp.                                                         | Log in and navigate to the community page to check if posts are displayed properly.                                                | ✅         |
| **Submit a post**               | Users should be able to type and submit new posts.                                                                                             | Log in, write a post, and submit it. Verify if it appears in the list of posts.                                                    | ✅         |
| **Edit a post**                 | Users should be able to edit only their own posts.                                                                                             | Log in, edit one of your posts, and check if changes are saved. Try editing another user’s post.                                   | ✅         |
| **Delete a post**               | Users should be able to delete only their own posts.                                                                                           | Log in, delete one of your posts, and check if it disappears. Try deleting another user’s post.                                    | ✅         |
| **Add a dialysis record**       | Users should be able to add a dialysis record only when logged in. The form should have all required fields.                                   | Log in and attempt to add a dialysis record. Check if the form accepts valid inputs and shows errors for missing fields.           | ✅         |
| **View past records**           | Users should be able to view only their own past dialysis records.                                                                             | Log in, navigate to the records page, and verify if only personal records are visible.                                             | ✅         |
| **Calendar**                    | Users should be able to view a calendar displaying a monthly view by default. Clicking a date should show events.                              | Log in, go to the calendar, and check if it displays properly. Click on a date to see event details.                               | ✅         |
| **Add an event or appointment** | Users should be able to add a calendar event only when logged in. Required fields should be validated.                                         | Log in and try to add an event with complete and incomplete inputs. Verify error messages and database storage.                    | ✅         |
| **Edit calendar event**         | Users should be able to edit only their own calendar events.                                                                                   | Log in, attempt to edit an event you created, and check if the changes are saved. Try editing another user’s event.                | ✅         |
| **Delete calendar event**       | Users should be able to delete only their own calendar events.                                                                                 | Log in, delete one of your events, and confirm it is removed. Try deleting another user’s event.                                   | ✅         |
| **Upload document**             | Users should be able to upload PDFs, PNGs, and JPEGs (max size: 5MB) only when logged in.                                                      | Log in, try uploading valid and invalid files (e.g., unsupported formats, large files). Check if files are stored and retrievable. | ✅         |

### Login and Register

![Login/Register Demo](https://res.cloudinary.com/dzibrzlq9/image/upload/v1741481433/login-register_ic4imh.gif)

### Community

![Community Demo](https://res.cloudinary.com/dzibrzlq9/image/upload/v1741482079/community_1_lxiphb.gif)

### Records

![Records Demo](https://res.cloudinary.com/dzibrzlq9/image/upload/v1741481435/recordss_ja4fid.gif)

### Uploads

![Uploads Demo](https://res.cloudinary.com/dzibrzlq9/image/upload/v1741481434/uploads_mmcmgj.gif)

### Calendar

![Calendar demo](https://res.cloudinary.com/dzibrzlq9/image/upload/v1741528804/calendarr_upqyek.gif)

## Automated Testing

## Djang Unit Tests

### Users - Login and Sign up

![Users Tests](https://res.cloudinary.com/dzibrzlq9/image/upload/v1741623554/users_test_xxcsoc.png)

### Community

![Community Tests](https://res.cloudinary.com/dzibrzlq9/image/upload/v1741623491/community_test_hxi2dl.png)

### Calendar

![Calendar Tests](https://res.cloudinary.com/dzibrzlq9/image/upload/v1741623476/calendar_test_nzukcs.png)

### Records

![Records Tests](https://res.cloudinary.com/dzibrzlq9/image/upload/v1741623508/records_test_mptfv7.png)

### Uploads

![Uploads Tests](https://res.cloudinary.com/dzibrzlq9/image/upload/v1741623530/uploads_test_jywzk9.png)

## HTML Validation Tests

- **HTML Validation**: Used the [W3C HTML Validator](https://validator.w3.org/) which returned the following results:

![HTML Validation](https://res.cloudinary.com/dzibrzlq9/image/upload/v1741776880/html_whfkh0.png)

## CSS Validation Tests

- **CSS Validation**: Used the [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) which returned the following results:

![CSS Validation](https://res.cloudinary.com/dzibrzlq9/image/upload/v1741776868/css_qumr2s.png)

## Javascript Validation Tests

- **JavaScript Validation**: Used [JSHint](https://jshint.com/) to validate JavaScript code

![calendar.js](https://res.cloudinary.com/dzibrzlq9/image/upload/v1741719302/jshint_cragmi.png)

## Python Validation Tests

- **Python Validation**: Used [CI Python Linter](https://pep8ci.herokuapp.com/) to validate Python code. My website comprises of 7 apps with an average of 4 python files each. I have tested all of them but attaching all the screenshots will overcrowd this document. I have cleaned them up according to the pep8 report. There are few others that shortning the character length would beat pep8 purpose of readability as they were only one character over the limit and sometimes it would just be a closing bracket.

![Passed Validation](https://res.cloudinary.com/dzibrzlq9/image/upload/v1741778048/errror_none_d2vo8p.png)

![Validation Fail](https://res.cloudinary.com/dzibrzlq9/image/upload/v1741778048/error_yes_d8uakr.png)

## Lighthouse Scores

- **Lighthouse Scores**: Used [Lighthouse Metrics](https://lighthouse-metrics.com/) to measure the scores

### Scores for Home Page

![Home](https://res.cloudinary.com/dzibrzlq9/image/upload/v1741779211/lighthouse_home_wqsuy4.png)

### Scores for Dashboard

![Dashboard](https://res.cloudinary.com/dzibrzlq9/image/upload/v1741779210/lighthouse_dashboard_osmhbz.png)

## Browser Compatibility

The website was manually tested in chrome, firefox and edge and it worked accross those different browsers

## Accessibility

- **Accessibility**: Used [WAVE](https://wave.webaim.org/). I could only manage to test the pages that are accessible without login, for the other pages, I used the report I got from home page to clean them up.

![Accessibility](https://res.cloudinary.com/dzibrzlq9/image/upload/v1741775364/wave_home_lejwi3.png)

![Accessibility](https://res.cloudinary.com/dzibrzlq9/image/upload/v1741775365/wave_login_xygasm.png)

![Accessibility](https://res.cloudinary.com/dzibrzlq9/image/upload/v1741775365/wave_signup_glpfbf.png)

## Responsiveness

- **Responsiveness**: Used [Am I responsive](https://ui.dev/amiresponsive). I had to download Ignore X-frames extesion to be able to use the test. However, I could only manage to test the home page and login page as there was a security warning when I logged in.

![Responsiveness](https://res.cloudinary.com/dzibrzlq9/image/upload/v1741716797/responsive_home_qv2vst.png)

![Responsiveness](https://res.cloudinary.com/dzibrzlq9/image/upload/v1741716797/responsive_login_fdmh3o.png)

![Responsiveness](https://res.cloudinary.com/dzibrzlq9/image/upload/v1741716797/responsive_error_iur23j.png)
