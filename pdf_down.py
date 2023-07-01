import requests
from bs4 import BeautifulSoup

'''
URL of the archive web-page which provides link to
all pdf lectures. It would have been tiring to
download each pdf manually.
In this example, we first crawl the webpage to extract
all the links and then download pdfs.
'''

# specify the URL of the archive here
archive_url = "https://tim.blog/2018/09/20/all-transcripts-from-the-tim-ferriss-show/"

def get_pdf_links():
	
	# create response object
	r = requests.get(archive_url)
	
	# create beautiful-soup object
	soup = BeautifulSoup(r.content,'html5lib')
	
	# find all links on web-page
	links = soup.findAll('a')

	# filter the link sending with .mp4
	pdf_links = [link['href'] for link in links if link['href'].endswith('pdf')]

	return pdf_links



def download_pdf_series(pdf_links):

	for link in pdf_links:

		'''iterate through all links in pdf_links
		and download them one by one'''
		
		# obtain filename by splitting url and getting
		# last string
		file_name = link.split('/')[-1]

		print( "Downloading file:%s"%file_name)
		
		# create response object
		r = requests.get(link, stream = True)
		
		# download started
		with open(file_name, 'wb') as f:
			for chunk in r.iter_content(chunk_size = 1024*1024):
				if chunk:
					f.write(chunk)
		
		print( "%s downloaded!\n"%file_name )

	print ("All pdfs downloaded!")
	return


if __name__ == "__main__":

	# getting all pdf links
    pdf_links = get_pdf_links()

# download all pdfs
download_pdf_series(pdf_links)
