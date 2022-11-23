import app_package_mcndoungerii.app as object

# from app_package_mcndoungerii.model import General

# #create a class object
# object = General()
class TestApp:

    print("Object::::::::::::",object)

    # def test_upper(self):
    #     assert object.upper_case("juma") == "JUMA"

    def test_lower(self):
        assert object.lower_case("TOYOTA") == "toyota"

    # def test_is_title(self):
    #     assert object.is_title("Toyota") == True