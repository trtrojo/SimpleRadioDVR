from podgen import Podcast, Episode, Media
# Create the Podcast
p = Podcast(
   name="Animals Alphabetically",
   description="Every Tuesday, biologist John Doe and wildlife "
               "photographer Foo Bar introduce you to a new animal.",
   website="http://example.org/animals-alphabetically",
   explicit=False,
)
# Add some episodes
p.episodes += [
   Episode(
     title="Aardvark",
     media=Media("http://example.org/files/aardvark.mp3", 11932295),
     summary="With an English name adapted directly from Afrikaans "
             '-- literally meaning "earth pig" -- this fascinating '
             "animal has both circular teeth and a knack for "
             "digging.",
   ),
   Episode(
      title="Alpaca",
      media=Media("http://example.org/files/alpaca.mp3", 15363464),
      summary="Thousands of years ago, alpacas were already "
              "domesticated and bred to produce the best fibers. "
              "Case in point: we have found clothing made from "
              "alpaca fiber that is 2000 years old. How is this "
              "possible, and what makes it different from llamas?",
   ),
]
# Generate the RSS feed
rss = p.rss_str()