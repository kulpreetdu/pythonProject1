REM pytest -s -v -m  "regression"  --html=./reports/report.html test_cases/test_login_page.py/
pytest -v -s test_cases/test_login_negative.py --html=reports/report.html -m  "regression or smoke"
REM pytest -v -s test_cases/test_add_cust_page.py --html=./reports/report.html -m  "regression or smoke"
REM pytest -v -s test_cases/test_search_cust_page.py --html=./reports/report.html -m  "regression or smoke"
REM pytest -v -s test_cases/test_search_cust_page_email_name.py --html=./reports/report.html -m  "regression or smoke"