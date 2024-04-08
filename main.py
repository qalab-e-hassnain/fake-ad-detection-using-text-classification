from src.Model_API import predict_ML

if __name__ == "__main__":
    ad_url = "https://www.pakwheels.com/used-cars/suzuki-mehran-2015-for-sale-in-bahawalpur-8558017"
    result = predict_ML(ad_url)
    result = "Dealer" if result == 1 else "Genuine"
    print(result)
    print("Success")
