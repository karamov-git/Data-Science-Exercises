def assertion(expected_data, actual_data):
	try:
		assert(expected_data.equals(actual_data)), 'Wrong answer, try again'
		print('Correct answer!')
		return actual_data.head()
	except AssertionError as err:
		print(err)
		return None
		

import pandas as pd
tips_data = pd.read_csv("tips.csv")


def assert_task1(actual_data):
	expecte_data = tips_data[tips_data.tip == 10]
	return  assertion(expecte_data, actual_data)

	
def assert_task2(actual_data):
	expecte_data = tips_data[tips_data["size"].between(5, 6)]
	return  assertion(expecte_data, actual_data)

	
def assert_task3(actual_data):
	expecte_data = tips_data[tips_data.smoker == "Yes"]
	return  assertion(expecte_data, actual_data)
	
	
def assert_task4(actual_data):
	expecte_data = tips_data[tips_data.smoker == "No"]
	return  assertion(expecte_data, actual_data)

	
def assert_task5(actual_data):
	expecte_data = tips_data[tips_data.tip.isin([5, 7, 10])]
	return  assertion(expecte_data, actual_data)
	
	
def assert_task6(actual_data):
	expecte_data = tips_data[tips_data.day.isin(["Sat", "Sun"])]
	return  assertion(expecte_data, actual_data)

	
def assert_task7(actual_data):
	expecte_data = tips_data[(tips_data["size"] > 4) & (tips_data.sex == "Female")]
	return  assertion(expecte_data, actual_data)


def assert_task8(actual_data):
	expecte_data = tips_data[(tips_data.total_bill > 40) & (tips_data.tip > 5)]
	return  assertion(expecte_data, actual_data)


def assert_task9(actual_data):
	expecte_data = tips_data[(tips_data["size"] > 4) | (tips_data.time == "Dinner")]
	return  assertion(expecte_data, actual_data)


def assert_task10(actual_data):
	smoker_filter = tips_data.smoker == "No"
	total_bill_filter = tips_data.total_bill > 30
	day_filter = tips_data.day.isin(["Thur", "Fri"])
	all_filters = smoker_filter & total_bill_filter & day_filter
	expecte_data = tips_data[all_filters]
	return  assertion(expecte_data, actual_data)

	
def assert_task11(actual_data):
	day_filter = tips_data.day.isin(["Fri", "Sat"])
	time_filter = tips_data.time == "Lunch"
	size_filter = tips_data["size"] < 4
	all_filters = day_filter & time_filter & size_filter
	expecte_data = tips_data[all_filters]
	return  assertion(expecte_data, actual_data)

	
def assert_task12(actual_data):
	first_filter = (tips_data.day == "Fri") & (tips_data["size"] < 3) & (tips_data.sex == "Female")
	second_filter = (tips_data.day == "Sun") & (tips_data["size"] > 4) & (tips_data.sex == "Male")
	all_filters = first_filter | second_filter

	expecte_data = tips_data[all_filters]
	return  assertion(expecte_data, actual_data)


