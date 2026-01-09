from behave import given, when, then

@given('user is on login page')
def step_impl(context):
    context.page.goto("https://practicetestautomation.com/practice-test-login/")

@when('user login with valid credentials')
def step_impl(context):
    context.page.fill("#username", "student")
    context.page.fill("#password", "Password123")
    context.page.click("#submit")

@when('user submit application')
def step_impl(context):
    # Already redirected after login, nothing extra needed
    pass

@then('application should be submitted successfully')
def step_impl(context):
    assert context.page.is_visible(".post-title")

@when('user login with invalid credentials')
def step_impl(context):
    context.page.fill("#username", "wrong")
    context.page.fill("#password", "wrong")
    context.page.click("#submit")

@then('error message should be displayed')
def step_impl(context):
    assert context.page.is_visible("#error")
