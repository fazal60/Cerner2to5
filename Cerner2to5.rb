require 'open-uri'
require 'nokogiri'

special_characters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-', '=', '{', '}', ':', ';', '<', '>', '?', ',', '.', '`', '~']

def raise_exception   
  puts 'Invalid special_character passed as input'  
  exit 1 
end 

unless ARGV && ARGV.length == 1
  	puts "Incorrect number of args. Correct usage: ruby Cerner2to5.rb <author_name>"
  	exit 1  
end

if special_characters.index(ARGV[0])
	raise_exception
end 

begin  
  	doc = Nokogiri::XML(open("https://www.goodreads.com/api/author_url/#{ARGV[0]}?key=gHMa4gvnE0Igcv2gaOIVWg"))
	id = doc.xpath("//*[@id]")[0].attr('id') #get book id
	author_name = doc.xpath("//name")[0].text #get author name
	puts "Author name closest to the one you passed in is '" + author_name + "'"
	books = Nokogiri::XML(open("https://www.goodreads.com/author/show/#{id}?format=xml&key=gHMa4gvnE0Igcv2gaOIVWg")) #reading books xml using Nokogiri
	puts "------Books by this author are as follows------"
	books.xpath("//title").each do |book| #printings books by the author passed in
		puts book.text
	end
rescue Exception => e  
  	puts "You have entered an invalid author name"
end  

