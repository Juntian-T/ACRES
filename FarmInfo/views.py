from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect

from .models import Farm, Crop, Client, Ownership, Farm_has_visit, Visit, Problem, Visit_has_problem, Problem_specifics, Problem_has_specifics
from .forms import CropForm, FarmForm, ClientForm, VisitForm, ProblemForm, ProblemSpecificForm

# .../FarmInfo page
def index(request):
	farm_list = Farm.objects.all()
	context = {'farm_list' : farm_list} # get the farms and store it in farm_list
	return render(request, 'FarmInfo/index.html', context) # send it to index.html template

# .../FarmInfo/1 etc. pages
def detail(request, farm_id):
	farm = get_object_or_404(Farm, pk=farm_id) # get the farm by id
	owner_id = Ownership.objects.get(farm_id=farm_id).client_id_id # get the farm's owner's id
	owner = Client.objects.get(pk=owner_id) # get the owner info
	return render(request, 'FarmInfo/detail.html', {'farm': farm, 'owner': owner}) # send these information to the detail.html template
	
# .../FarmInfo/addCrop page
def addCrop(request):
	if request.method == 'POST':
		form = CropForm(request.POST) # creates the form needed for adding a new Crop
		if form.is_valid():
			crop_name = form.cleaned_data['crop_name'] # get the Crop name from user's input (from the template/view)
			query = Crop(crop_name=crop_name) # query to add a new Crop
			query.save() # excute the query
			return HttpResponseRedirect('../') #redirect to homepage (may change later)
	else:
		form = CropForm() # an empty form is created if the method is not POST

	return render(request, 'FarmInfo/addCrop.html', {'form': form}) # sends the form to addCrop.html template


# .../FarmInfo/addFarm page
def addFarm(request):
	if request.method == 'POST':
		# creates two forms, one for adding Farm, one for adding Client
		farmForm = FarmForm(request.POST, prefix='form1')
		clientForm = ClientForm(request.POST, prefix='form2')

		if farmForm.is_valid() and clientForm.is_valid():
			# gets necessary information for adding the Farm
			farm_name = farmForm.cleaned_data['farm_name']
			city = farmForm.cleaned_data['city']
			state = farmForm.cleaned_data['state']
			address = farmForm.cleaned_data['address']
			office_num = farmForm.cleaned_data['office_num']
			fax = farmForm.cleaned_data['fax']
			web = farmForm.cleaned_data['web']
			notes = farmForm.cleaned_data['notes']

			# gets necessary information for adding the Client
			first_name = clientForm.cleaned_data['first_name']
			last_name = clientForm.cleaned_data['last_name']
			spouse = clientForm.cleaned_data['spouse']
			children = clientForm.cleaned_data['children']
			email = clientForm.cleaned_data['email']
			pet = clientForm.cleaned_data['pet']
			phone = clientForm.cleaned_data['phone']
			notes = clientForm.cleaned_data['notes']

			# query to add the Farm
			query1 = Farm(farm_name=farm_name, city=city, state=state, address=address, office_num=office_num, fax=fax, web=web, notes=notes)
			query1.save()

			# query to add the Client
			query2 = Client(first_name=first_name, last_name=last_name, spouse=spouse, children=children, email=email, pet=pet, phone=phone, notes=notes)
			query2.save()

			# the Client owns this Farm, so another entry is added to the Ownership table
			# however, this is not a robust way of getting the ids, becasue there might be other people adding farms at the same time
			farm_id = Farm.objects.latest('id')
			client_id = Client.objects.latest('id')

			query3 = Ownership(farm_id=farm_id, client_id=client_id)
			query3.save()

			

		return HttpResponseRedirect('../')
	else:
		farmForm = FarmForm(prefix='form1')
		clientForm = ClientForm(prefix='form2')

	return render(request, 'FarmInfo/addFarm.html', {'farmForm': farmForm ,'clientForm': clientForm}) # sends both forms to addFarm.html template

# 2/19/2016 ----- Hannah & JT -----------
# .../FarmInfo/addVisit/1 etc. pages
def addVisit(request, farm_id):
	if request.method == 'POST':
		#Three forms are needed for this page
		visitForm = VisitForm(request.POST, prefix='form1')
		problemForm = ProblemForm(request.POST, prefix='form2')
		problemSpecificForm = ProblemSpecificForm(request.POST, prefix='form3')

		if visitForm.is_valid() and problemForm.is_valid() and problemSpecificForm.is_valid():
			# collect user's input for visitForm
			visit_date = visitForm.cleaned_data['visit_date']

			# collect user's input for problemForm
			crop_name = problemForm.cleaned_data['crop_name']
			notes = problemForm.cleaned_data['notes']

			# collect user's input for problemSpecificForm
			type_name = problemSpecificForm.cleaned_data['type_name']
			specific_name = problemSpecificForm.cleaned_data['specific_name']

			# add the visit to database
			query_visit = Visit(visit_date=visit_date)
			query_visit.save()

			# add the problem to database
			farm = get_object_or_404(Farm, pk=farm_id)
			query_problem = Problem(farm_id=farm, crop_name=crop_name, notes=notes)
			query_problem.save()

			# check if this specifics already exists in Problem_specifics table
			num_results = Problem_specifics.objects.filter(name=specific_name, type_name=type_name).count()

			# only add if the pair does not exist before
			if (num_results == 0):
				query_problem_specifics = Problem_specifics(name=specific_name, type_name=type_name)
				query_problem_specifics.save()

			# use above information to add entry to Farm_has_visit (relation) 
			visit_id = Visit.objects.latest('id')
			farm = get_object_or_404(Farm, pk=farm_id)
			query_farm_has_visit = Farm_has_visit(farm_id=farm, visit_id=visit_id)
			query_farm_has_visit.save()

			# and Visit_has_problem table (relation)
			problem_id = Problem.objects.latest('id')
			query_visit_has_problem = Visit_has_problem(visit_id=visit_id, problem_id=problem_id)
			query_visit_has_problem.save()

			# and Problem_has_specifics (relation between the problem of a farm, and what the problem actually was)
			specific_id = Problem_specifics.objects.latest('id')
			query_problem_has_specifics = Problem_has_specifics(problem_id=problem_id, specific_id=specific_id)
			query_problem_has_specifics.save()

	else:
		visitForm = VisitForm(prefix='form1')
		problemForm = ProblemForm(prefix='form2')
		problemSpecificForm = ProblemSpecificForm(prefix='form3')
	return render(request, 'FarmInfo/addVisit.html', {'visitForm': visitForm, 'problemForm': problemForm, 'problemSpecificForm': problemSpecificForm})

# .../FarmInfo/viewVisits pages
def viewVisits(request, farm_id):
#    farm = get_object_or_404(Farm, pk=farm_id) # get the farm by id
#    # get all farm-visit relationships by the specific farm id
#    farm_visits = Farm_has_visit.objects.filter(pk=farm_id)
#    # get visit ids from farm_visits
# #    visit_ids = farm_visits.
#    visit_list = []
#    for idV in visit_ids:
#        # get visit dates by visit ids
#        vDate = Visit.objects.get(pk=visit_idV).visit_date
#        # create list of visit dates based on visit ids
#        visit_list.append(vDate)
   # return the farm and corresponding visit dates to viewVisits page
   return render(request, 'FarmInfo/viewVisits.html')

# .../FarmInfo/visitDetail pages
def visitDetail(request):
   return render(request, 'FarmInfo/visitDetail.html')