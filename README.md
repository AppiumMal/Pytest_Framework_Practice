1. Use virtual environment venv314 with python version 3.14
2..\venv314\Scripts\Activate.ps1
15/09/2026:
 
1.deleted all contents from .cache/selenium folder to activate new Chrome version.
2.python -m pip freeze > requirements.txt ---> you never have to install them one by one


1. A developer commits and pushes code to GitHub.

2. GitHub Actions triggers the CI pipeline automatically.

3. The pipeline creates a runner (temporary execution machine).

4. The latest source code is checked out onto the runner.

5. Dependencies are installed using:
   pip install -r requirements.txt

6. PyTest executes the required test suite
   (smoke, sanity, or regression).

7. HTML reports are generated showing passed and failed tests.

8. Screenshots captured for failed tests are collected as evidence.

9. Reports and screenshots are uploaded as pipeline artifacts for review.

10. The pipeline status is marked as Passed or Failed.

test_valid_login - @pytest.mark.smoke
test_invalid_login - @pytest.mark.regression
test_button_page_title - @pytest.mark.regression
test_single_click_button -@pytest.mark.sanity
test_multiple_click_button -@pytest.mark.sanity
test_navigation_to_home_page - @pytest.mark.smoke