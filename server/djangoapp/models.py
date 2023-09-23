from django.db import models
from django.utils.timezone import now


# Create your models here.

class CarMake(models.Model):
  name = models.CharField(max_length=100, null=False)
  description = models.CharField(max_length=500)
  
  def __str__(self):
    return "Name: " + self.name + "," + \
            "Description: " + self.description


class CarModel(models.Model):
  CAR_TYPES = (
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
    )
  
  car_make = models.ForeignKey(CarMake,on_delete=models.CASCADE)
  name = models.CharField(max_length=100, null=False)
  dealer_id = models.IntegerField()
  type = models.CharField(max_length=10, choices=CAR_TYPES)
  year = models.DateField(null=True)
  
  def __str__(self):
    return  "Name: "+self.name+", "+\
            "Dealer Id: "+str(self.dealer_id)+", "+\
            "Type: "+self.type+", "+\
            "Year: "+str(self.year)


class CarDealer:

    def __init__(self, address, city, id, lat, long, st, zip, full_name):
        # Dealer address
        self.address = address
        # Dealer city
        self.city = city
       
        # Dealer id
        self.id = id
        # Location lat
        self.lat = lat
        # Location long
        self.long = long

        # Dealer state
        self.st = st
        # Dealer zip
        self.zip = zip

        # Full name
        self.full_name = full_name

    def __str__(self):
        return "Dealer name: " + self.full_name


class DealerReview:
    def __init__(self, dealership, name, purchase, review):
        # Required attributes
        self.dealership = dealership
        self.name = name
        self.purchase = purchase
        self.review = review
        # Optional attributes
        self.purchase_date = ""
        self.purchase_make = ""
        self.purchase_model = ""
        self.purchase_year = ""
        self.sentiment = ""
        self.id = ""

    def __str__(self):
        return "Review: " + self.review

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__,sort_keys=True, indent=4)
