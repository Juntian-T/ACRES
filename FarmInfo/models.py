from django.db import models
import datetime
# This file defines what the database will look like
# Each class is a table, and its fields are columns in this table
class Client(models.Model):
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)
	spouse = models.CharField(max_length=200, blank=True)
	children = models.CharField(max_length=200, blank=True)
	email = models.CharField(max_length=200, blank=True)
	pet = models.CharField(max_length=200, blank=True)
	phone = models.CharField(max_length=200, blank=True)
	notes = models.TextField(blank=True)
	def __str__(self):
		return self.first_name + " " + self.last_name

class Farm(models.Model):
	farm_name = models.CharField(max_length=200)
	city = models.CharField(max_length=200)
	state = models.CharField(max_length=200)
	address = models.CharField(max_length=200)
	office_num = models.CharField(max_length=200, blank=True)
	fax = models.CharField(max_length=200, blank=True)
	web = models.CharField(max_length=200, blank=True)
	notes = models.TextField(blank=True)
	def __str__(self):
		return self.farm_name

class Crop(models.Model):
	crop_name = models.CharField(max_length=200, primary_key=True)
	def __str__(self):
		return self.crop_name

class Ownership(models.Model):
	farm_id = models.ForeignKey(Farm)
	client_id = models.ForeignKey(Client)

class Grows(models.Model):
	farm_id = models.ForeignKey(Farm)
	crop_name = models.ForeignKey(Crop, null=True)


# ------------ We chose to use the old design! 2/12/16--------------
class Visit(models.Model):
	# date
	visit_date = models.DateField(default=datetime.date.today)
	# def __str__(self):
	# 	return self.visit_date
	
class Problem(models.Model):
	farm_id = models.ForeignKey(Farm)
	crop_name = models.ForeignKey(Crop) # null = True is omitted
	notes = models.TextField(blank=True)
	img = models.ImageField(upload_to='images', default='images/default.png');
	# action_type 
	# def __str__(self):
	# 	return "Problem at farm" + self.farm_id

class Farm_has_visit(models.Model):
	farm_id = models.ForeignKey(Farm)
	visit_id = models.ForeignKey(Visit)

class Visit_has_problem(models.Model):
	visit_id = models.ForeignKey(Visit)
	problem_id = models.ForeignKey(Problem)

class Problem_type(models.Model):
	type_name = models.CharField(max_length=200, primary_key=True)
	def __str__(self):
		return self.type_name

class Problem_specifics(models.Model):
	name = models.CharField(max_length=200)
	type_name = models.ForeignKey(Problem_type)
	def __str__(self):
		return self.name

class Problem_has_specifics(models.Model):
	problem_id = models.ForeignKey(Problem)
	specific_id = models.ForeignKey(Problem_specifics)
	

# 01/29/16 MS & JT

# class Insect(models.Model):
# 	insect_name = models.CharField(max_length=200)
# 	def __str__(self):
# 		return self.insect_name

# class Disease(models.Model):
# 	diesase_name = models.CharField(max_length=200)
# 	def __str__(self):
# 		return self.diesase_name


# ---------- Designs up to 2/2 --------------

# class Visit(models.Model):
# 	# date
# 	visit_date = models.DateField(default=datetime.date.today)
	
# class Problem(models.Model):
# 	farm_id = models.ForeignKey(Farm)
# 	crop_name = models.ForeignKey(Crop) # null = True is omitted
# 	notes = models.TextField(blank=True)
# 	# action_type 

# class Farm_has_visit(models.Model):
# 	farm_id = models.ForeignKey(Farm)
# 	visit_id = models.ForeignKey(Visit)

# class Visit_has_problem(models.Model):
# 	visit_id = models.ForeignKey(Visit)
# 	problem_id = models.ForeignKey(Problem)

# class Problem_type(models.Model):
# 	type_name = models.CharField(max_length=200)

# class Problem_specifics(models.Model):
# 	name = models.CharField(max_length=200)
# 	type_id = models.ForeignKey(Problem_type)

# class Problem_has_specifics(models.Model):
# 	problem_id = models.ForeignKey(Problem)
# 	specific_id = models.ForeignKey(Problem_specifics)


# ---------- Designs from 2/3 -----------------
# class Visit(models.Model):
# 	# date
# 	visit_date = models.DateField(default=datetime.date.today)
# 	notes = models.TextField(blank=True)

# class Problem_type(models.Model):
# 	type_name = models.CharField(max_length=200)

# class Problem(models.Model):
# 	crop_name = models.ForeignKey(Crop) # null = True is omitted
# 	problem_type = models.ForeignKey(Problem_type)
# 	#problem_name = models.CharField(max_length=300)
# 	notes = models.TextField(blank=True)
# 	# action_type 

# # class Visit_has_problem(models.Model):
# # 	visit_id = models.ForeignKey(Visit)
# # 	problem_id = models.ForeignKey(Problem)

# class Farm_has_visit(models.Model):
# 	farm_id = models.ForeignKey(Farm)
# 	visit_id = models.ForeignKey(Visit)

