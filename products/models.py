from django.db import models

# Create your models here.
# model for products

class Product(models.Model):
    LIVE = 1
    DELETE = 0 # ഇത് രണ്ട് സ്ഥിരമായ മൂല്യങ്ങൾ (“constants”) ആണ്. ഒരു പ്രോഡക്ട് ഇപ്പോഴും ലൈവ് ആണോ അല്ലെങ്കിൽ “ഡിലീറ്റ് ചെയ്ത” സ്ഥിതിയിലോയെന്ന് സൂചിപ്പിക്കാൻ ഉപയോഗിക്കും.
    DELETE_CHOICES = ((LIVE,'live'),(DELETE,'Delete')) # delete_status ഫീൽഡിന് കൊടുക്കാനുള്ള  ("choices") ആണ് ഇത്. ഡാറ്റാബേസിൽ 1 വച്ചാൽ അത് “Live” ആയി കാണിക്കും, 0 വച്ചാൽ “Delete” ആയി. സെലക്ട് ചെയ്യാവുന്ന ഒരു ലിസ്റ്റ് പോലെ ആണ് ഇത്.

    title = models.CharField(max_length=200)
    price = models.FloatField()
    discription = models.TextField()
    image = models.ImageField(upload_to='product_images/')  # we'll fix this too #media settings.py grace app സാധാരണ ആയി upload_to-യിൽ റൂട്ടിനും MEDIA_ROOT & MEDIA_URL സെറ്റിംഗുകളും ശരിയായി Django settings.py-ൽ ക്രമീകരിച്ചിരിക്കണം
    priority = models.IntegerField(default=0) # പ്രോഡക്ടിന്റെ പ്രാധാന്യം/ക്രമദ്രുട്ടി സൂചിപ്പിക്കാൻ ഉപയോഗിക്കാൻ കഴിയുന്ന ഒരു integer. ഡീഫോൾട്ടായി 0 എടുക്കുന്നു.
    delete_status = models.IntegerField(choices=DELETE_CHOICES,default=LIVE) # ഈ ഫീൽഡ് Product “ജീവിച്ചിരിക്കുന്നതാണോ” അല്ലെങ്കിൽ “ഡിലീറ്റ് ചെയ്തത്” ആണോ എന്ന് സൂചിപ്പിക്കുന്നത്.#choices ഉപയോഗിക്കുന്നത് admin interface-ൽ dropdown ആയി കാണിക്കാൻ സഹായിക്കും.#default=LIVE കൊണ്ട് പുതിയ പ്രോഡക്ട് ലൈവ് ആയി ഉണ്ടാവും.
    created_at = models.DateTimeField(auto_now=True) # object ആദ്യമായി ഗ്രന്ഥത്തിൽ (database) സൃഷ്ടിച്ച നേരം auto ആയി സെറ്റ് ചെയ്യും.  പിന്നീട് മാറുന്നില്ല
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):   # __str__ method ചേർക്കുക (admin, shell തുടങ്ങിയവയിൽ readable ആയി കാണാൻ):
        return self.title



