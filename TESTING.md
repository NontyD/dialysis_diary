## Manual Testing

| **Feature**                     | **Expectation**                                                                                                                                | **Test**                                                                                                                           | **Result** |
| ------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| **Sign-up feature**             | Users should be able to create an account by entering an email, username, and password. Errors should be displayed for taken usernames/emails. | Attempt to sign up with unique and duplicate credentials. Check if appropriate error messages appear.                              | ✅       |
| **Sign-in feature**             | Users should be able to log in using valid credentials and authentication should fail for invalid credentials.                                 | Attempt to log in with correct and incorrect credentials.                                                                          | ✅       |
| **View posts**                  | Users should be able to see a list of posts, including author, content, and timestamp.                                                         | Log in and navigate to the community page to check if posts are displayed properly.                                                | ✅       |
| **Submit a post**               | Users should be able to type and submit new posts.                                                                                             | Log in, write a post, and submit it. Verify if it appears in the list of posts.                                                    | ✅       |
| **Edit a post**                 | Users should be able to edit only their own posts.                                                                                             | Log in, edit one of your posts, and check if changes are saved. Try editing another user’s post.                                   | ✅       |
| **Delete a post**               | Users should be able to delete only their own posts.                                                                                           | Log in, delete one of your posts, and check if it disappears. Try deleting another user’s post.                                    | ✅       |
| **Add a dialysis record**       | Users should be able to add a dialysis record only when logged in. The form should have all required fields.                                   | Log in and attempt to add a dialysis record. Check if the form accepts valid inputs and shows errors for missing fields.           | ✅       |
| **View past records**           | Users should be able to view only their own past dialysis records.                                                                             | Log in, navigate to the records page, and verify if only personal records are visible.                                             | ✅       |
| **Calendar**                    | Users should be able to view a calendar displaying a monthly view by default. Clicking a date should show events.                              | Log in, go to the calendar, and check if it displays properly. Click on a date to see event details.                               | ✅       |
| **Add an event or appointment** | Users should be able to add a calendar event only when logged in. Required fields should be validated.                                         | Log in and try to add an event with complete and incomplete inputs. Verify error messages and database storage.                    | ✅       |
| **Edit calendar event**         | Users should be able to edit only their own calendar events.                                                                                   | Log in, attempt to edit an event you created, and check if the changes are saved. Try editing another user’s event.                | ✅       |
| **Delete calendar event**       | Users should be able to delete only their own calendar events.                                                                                 | Log in, delete one of your events, and confirm it is removed. Try deleting another user’s event.                                   | ✅       |
| **Upload document**             | Users should be able to upload PDFs, PNGs, and JPEGs (max size: 5MB) only when logged in.                                                      | Log in, try uploading valid and invalid files (e.g., unsupported formats, large files). Check if files are stored and retrievable. | ✅      |

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


## Unit Tests

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