from django.shortcuts import render, redirect
from django import forms
from.models import Listing, RenteeUser, Category, GalleryImage
# from .forms import ListingForm
from django.http import HttpResponseRedirect

# Create your views here.

def Homepage(request):
    listings = Listing.objects.all()
    categorys = Category.objects.all()
    return render(request, 'Home/Home.html',{
        'listings': listings,
        'categorys':categorys,
    })


def Searchpage(request):
    if request.method=='POST':
        Searched=request.POST['Searched']
        listings = Listing.objects.filter(Name__contains=Searched)
        withcost_listings = Listing.objects.filter(MonthlyRate__contains=Searched)
        return render(request, 'Home/Search.html', {
           'Searched': Searched,
           'listings': listings,
           'withcost_listings':withcost_listings,
        })
    else:
        return render(request, 'Home/Search.html', {})

        

def ViewListing(request, listing_id):
    listing = Listing.objects.get(pk=listing_id)
    return render (request, 'Home/ViewListing.html', {
        'listing':listing,
    })


# add listing with django forms
# def AddListing(request):
#     submitted = False
#     if request.method=='POST':
#         form=ListingForm(request.POST, request.FILES)
#         if form.is_valid():
#             listing = form.save(commit=False)
#             listing.Owner=request.user.id
#             # listing.Owner=request.user
#             listing.save()
#             return HttpResponseRedirect('/AddListing?submitted=True')
#     else:
#         form=ListingForm
#         if 'submitted' in request.GET:
#             submitted=True
#     return render(request, 'Home/AddListing.html',{
#         'submitted':submitted,
#         'form':form
#     })

def AddListing(request):
    if request.method=='POST':
        Name=request.POST['Name']
        Location=request.POST['Location']
        Description=request.POST['Description']
        MonthlyRate=request.POST['MonthlyRate']
        ListingImage=request.FILES.get('ListingImage')
        # ListingImage=request.POST['ListingImage']
        NumberOfBedrooms=request.POST['NumberOfBedrooms']
        Contact=request.POST['Contact']
        AreaOccupied=request.POST['AreaOccupied']
        # ListingGallery=request.POST['ListingGallery']
        # ListingGallerys=request.FILES.getlist('ListingGallerys')

        NewListing=Listing(
            Name=Name,
            Location=Location,
            Description=Description, 
            NumberOfBedrooms=NumberOfBedrooms, 
            AreaOccupied=AreaOccupied, 
            MonthlyRate=MonthlyRate, 
            ListingImage=ListingImage, 
            Contact=Contact,
        )
        NewListing.save()
        return redirect ('AddlistingGallery', listing_id = NewListing.id)
            


    return render (request, 'Home/AddListing.html', {})
   
def AddlistingGallery(request, listing_id):
    # listing = Listing.objects.get(pk=listing_id)
    if request.method=='POST':
        Images=request.FILES.getlist('Images')
        Name=request.POST['Name']
        # Gallery_list=[]

        # new_ListingGallery2=ListingGallery2(Gallery=Gallery)
        # new_ListingGallery2.save()

        for Image in Images:
            new_GalleryImage=GalleryImage(
                Image=Image,
                Listing = Listing.objects.get(pk=listing_id),
                Name=Name,
            )
            new_GalleryImage.save()
        print(Images)
        return redirect ('home')


            # Gallery_list.append(new_Gallery.Gallery)


    return render (request, 'Home/AddlistingGallery.html', {

    } )

# def ViewCategories(request, Category_id):
#     category = Category.objects.get(pk=category_id)
#     return render (request, 'Home/ViewListing.html', {
#         'category':category
#     })

# def VisitCategory(request):
#     viewcategory = Category.objects.all()
#     return render(request, 'Home/Home.html',{
#         'viewcategory': viewcategory
        
#     })












