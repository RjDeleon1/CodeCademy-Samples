## Start of class
class Art:
  def __init__(self, artist, title, medium, year, owner):
    self.artist = artist
    self.title = title
    self.medium = medium
    self.year = year
    self.owner = owner

  def __repr__(self):
    return f"{self.artist}. '{self.title}'.  {self.medium}. {self.year}. {self.owner.name}. {self.owner.location}."
## End of class


## Start of class
class Marketplace:
  def __init__(self, listings = []):
    self.listings = listings
  
  def add_listing(self, new_listing):
    self.listings.append(new_listing)
  
  def remove_listing(self, listing):
    self.listings.remove(listing)

  def show_listings(self):
    return self.listings


## end of Class

## Start of class
class Client:
  def __init__(self, name, location, is_museum):
    self.name = name
    self.location = location
    self.is_museum = is_museum
  
  def sell_artwork(self, artwork, price):
    if artwork.owner == self:
      new_Listing = Listing(artwork, price, self)
      veneer.add_listing(new_Listing)

  def buy_artwork(self, artwork):
    if artwork.owner != self:
      art_listing = None
      for listing in veneer.listings:
        if listing.art == artwork:
          art_listing = listing
          break
      if art_listing != None:
        artwork.owner = self
        veneer.remove_listing(art_listing)


      
## End of class


## Start of class
class Listing:
  def __init__(self, art, price, seller):
    self.art = art
    self.price = price
    self.seller = seller
  
  def __repr__(self):
    return f"The price for {self.art} is {self.price}"

  
## End of class

veneer = Marketplace()

edytta = Client("Edytta Halpirt", "Private Collection", False)

girl_with_mandolin = Art("Picasso, Pablo", "Girl with a Mandolin (Fanny Tellier)", 1910, "oil on canvas", edytta)


moma = Client("The MOMA", "New York", True)


edytta.sell_artwork(girl_with_mandolin, "$6M (USD)")

print(veneer.show_listings())

moma.buy_artwork(girl_with_mandolin)

print(girl_with_mandolin)

print(veneer.show_listings())
