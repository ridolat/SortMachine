# ANALYSIS

# 1. Write a GUI program that:
# Is a sort machine
# - Contains widgets
# - Buttons
# - Labels
# - Dropdown Box
# - Text box for description

# 2. Output to Monitor
# - GUI Window that Contains Widgets as stated above
# - GIF's with different sort methods, selected by the user

# 3. Purpose
# - See different sorts in action (Just a mini-project)


# 4. Processes
# - Shows GIF depending on user selection


#---------------------------------------------------------------------------



from Tkinter import *
from PIL import *
import os, sys, time

#Global Time Delay Value
timeDelayForBubble = 0.009999
timeDelayForSelection = 0.20
numOfImages = 0

# Explanations of all of the sorts
bubbleSortExplained = "Bubble Sort: \n A simple sorting algorithm that works by repeatedly stepping \n through the list to be sorted, comparing each pair of adjacent items \n and swapping them if they are in the wrong order."
selectionSortExplained = "Selection Sort: \n A sorting algorithm that divides the input list into two \n parts: the sublist of items already sorted, which is built up from left to right at the front (left) of the list, and the \n sublist of items remaining to be sorted that occupy the rest of the list. Initially, the sorted sublist is empty and the unsorted \n sublist is the entire input list. The algorithm proceeds by finding the smallest (or largest, depending on sorting order) element in the unsorted \n sublist, exchanging it with the leftmost unsorted element (putting it in sorted order), and moving the sublist boundaries one element to the right."
insertionSortExplained = "Insertion Sort: \n A sorting algorithm that iterates, consuming one input element \n each repetition, and growing a sorted output list. Each iteration, insertion sort removes one element \n from the input data, finds the location it belongs within the sorted list, and inserts it there. It \n repeats until no input elements remain."
mergeSortExplained = "Merge Sort: \n A sorting algorithm that divides the unsorted list into n sublists, then \n repeatedly merges sublists to produce new sorted sublists until \n there is only 1 sublist remaining."
heapSortExplained = "Heap Sort: \n A sorting algorithm that requires a heap be built out of the data.  The heap \n is often placed in an array with the layout of a complete binary tree. \n Then,  a sorted array is created by repeatedly removing the largest element from the heap (the root of the heap), and inserting it\n into the array. The heap is updated after each removal to maintain the heap. Once all objects have been removed \n from the heap, the result is a sorted array."
quickSortExplained = "Quick Sort: \n A sorting algorithm that first divides a large array into two smaller sub-array: \n the low elements and the high elements. Quicksort can then recursively sort the sub-arrays"

class SortMachineGUI:

	#define constructor
	def __init__(self):

		

		#Create window
		self.mainWindow = Tk()
		
		self.mainWindow.wm_title("Sort Machine");


		#Setup
		os.chdir("./BubbleSortImages/")

		#Sorts used in this program
		sortOptions = ["Select One", "BubbleSort", "SelectionSort", "InsertionSort", "MergeSort", "HeapSort","QuickSort"]
		

		#Get max size of canvas
		testImage = PhotoImage(file="tmp-0.gif")
		testWidth=testImage.width()
		testHeight=testImage.height()
		
		
		#Add Frames
		self.topFrame = Frame(self.mainWindow)
		self.middleFrame = Frame(self.mainWindow, background="BLACK", borderwidth=1, relief=SUNKEN)
		self.bottomFrame = Frame(self.mainWindow)

		#Add Widgets to frames
		self.gifCanvas = Canvas(self.topFrame, width=testWidth, height=testHeight)

		#Middle Frame
		self.sortLabel = StringVar() 
		self.sortLabel.set("Explanation Will Be Here")
		

		#Bottom Frame

		self.variable = StringVar(self.mainWindow)
		self.variable.set(sortOptions[0]) #default
		#Dropdown menu
		self.sortSelector = apply(OptionMenu, (self.bottomFrame, self.variable)+ tuple(sortOptions))

		self.startButton = Button(self.bottomFrame, text="Start Sort", command=self.startSort)

		#Pack Frames & Widgets
		self.topFrame.pack()
		self.middleFrame.pack()
		self.bottomFrame.pack()

		self.gifCanvas.pack()
		Label(self.middleFrame, textvariable=self.sortLabel).pack()
		self.sortSelector.pack(side=("left"))
		self.startButton.pack(side=("right"))


		mainloop()


	#Callback methods


	def startSort(self):
		sortSelected = self.variable.get()
		if (sortSelected == "BubbleSort"):
			print ("Bubble sort selected")
			self.sortLabel.set(bubbleSortExplained)
			bubbleSortFunction(self)
			self.sortLabel.set("Explanation Will Be Here")

		elif (sortSelected == "SelectionSort"):
			print ("Selection sort selected")
			self.sortLabel.set(selectionSortExplained)
			selectionSortFunction(self)
			self.sortLabel.set("Explanation Will Be Here")

		elif (sortSelected == "InsertionSort"):
			print ("Insertion sort selected")
			self.sortLabel.set(insertionSortExplained)
			insertionSortFunction(self)
			self.sortLabel.set("Explanation Will Be Here")

		elif (sortSelected == "MergeSort"):
			print ("Merge sort selected")
			self.sortLabel.set(mergeSortExplained)
			mergeSortFunction(self)
			self.sortLabel.set("Explanation Will Be Here")

		elif (sortSelected == "HeapSort"):
			print ("Heap sort selected")
			self.sortLabel.set(heapSortExplained)
			heapSortFunction(self)
			self.sortLabel.set("Explanation Will Be Here")

		elif (sortSelected == "QuickSort"):
			print ("Quick sort selected")
			self.sortLabel.set(quickSortExplained)
			quickSortFunction(self)
			self.sortLabel.set("Explanation Will Be Here")
			
		elif (sortSelected == "Select One"):
			print ("Do nothing")
		else:
			print ("Fix")

#Print out gif of bubble sort (same for all, except they are all different sorts)
def bubbleSortFunction(self):
	self.startButton.config(state=DISABLED)
	os.chdir("..")
	os.chdir("./BubbleSortImages/")
	testImage = PhotoImage(file="tmp-0.gif")
	testWidth=testImage.width()
	testHeight=testImage.height()
	numOfImages = len([name for name in os.listdir('.') if os.path.isfile(name)])
	for num in range (0, numOfImages):
		print (testImage)
		testImage = PhotoImage(file="tmp-"+str(num)+".gif")
		self.gifCanvas.create_image(testWidth/2, testHeight/2, image = testImage)
		self.gifCanvas.update()
		time.sleep(timeDelayForBubble)
	testImage = PhotoImage(file="tmp-"+str(numOfImages-1)+".gif")
	self.gifCanvas.create_image(testWidth/2, testHeight/2, image = testImage)
	self.gifCanvas.update()
	time.sleep(5)
	self.startButton.config(state=ACTIVE)

def selectionSortFunction(self):
	self.startButton.config(state=DISABLED)
	os.chdir("..")
	os.chdir("./SelectionSortImages/")
	testImage = PhotoImage(file="tmp-0.gif")
	testWidth=testImage.width()
	testHeight=testImage.height()
	numOfImages = len([name for name in os.listdir('.') if os.path.isfile(name)])
	for num in range (0, numOfImages):
		print (testImage)
		testImage = PhotoImage(file="tmp-"+str(num)+".gif")
		self.gifCanvas.create_image(testWidth+200, testHeight-50, image = testImage)
		self.gifCanvas.update()
		time.sleep(timeDelayForSelection)
	testImage = PhotoImage(file="tmp-"+str(numOfImages-1)+".gif")
	self.gifCanvas.create_image(testWidth+200, testHeight-50, image = testImage)
	self.gifCanvas.update()
	time.sleep(5)
	self.startButton.config(state=ACTIVE)

def insertionSortFunction(self):
	self.startButton.config(state=DISABLED)
	os.chdir("..")
	os.chdir("./InsertionSortImages/")
	testImage = PhotoImage(file="tmp-0.gif")
	testWidth=testImage.width()
	testHeight=testImage.height()
	numOfImages = len([name for name in os.listdir('.') if os.path.isfile(name)])
	for num in range (0, numOfImages):
		print (testImage)
		testImage = PhotoImage(file="tmp-"+str(num)+".gif")
		self.gifCanvas.create_image(testWidth/2, testHeight/2, image = testImage)
		self.gifCanvas.update()
		time.sleep(timeDelayForBubble)
	testImage = PhotoImage(file="tmp-"+str(numOfImages-1)+".gif")
	self.gifCanvas.create_image(testWidth/2, testHeight/2, image = testImage)
	self.gifCanvas.update()
	time.sleep(5)
	self.startButton.config(state=ACTIVE)


def mergeSortFunction(self):
	self.startButton.config(state=DISABLED)
	os.chdir("..")
	os.chdir("./MergeSortImages/")
	testImage = PhotoImage(file="tmp-0.gif")
	testWidth=testImage.width()
	testHeight=testImage.height()
	numOfImages = len([name for name in os.listdir('.') if os.path.isfile(name)])
	for num in range (0, numOfImages):
		print (testImage)
		testImage = PhotoImage(file="tmp-"+str(num)+".gif")
		self.gifCanvas.create_image(testWidth-50, testHeight/2+30, image = testImage)
		self.gifCanvas.update()
		time.sleep(timeDelayForBubble)
	testImage = PhotoImage(file="tmp-"+str(numOfImages-1)+".gif")
	self.gifCanvas.create_image(testWidth-50, testHeight/2+30, image = testImage)
	self.gifCanvas.update()
	time.sleep(5)
	self.startButton.config(state=ACTIVE)

def heapSortFunction(self):
	self.startButton.config(state=DISABLED)
	os.chdir("..")
	os.chdir("./HeapSortImages/")
	testImage = PhotoImage(file="tmp-0.gif")
	testWidth=testImage.width()
	testHeight=testImage.height()
	numOfImages = len([name for name in os.listdir('.') if os.path.isfile(name)])
	for num in range (0, numOfImages):
		print (testImage)
		testImage = PhotoImage(file="tmp-"+str(num)+".gif")
		self.gifCanvas.create_image(testWidth-100, testHeight/2+30, image = testImage)
		self.gifCanvas.update()
		time.sleep(timeDelayForBubble)
	testImage = PhotoImage(file="tmp-"+str(numOfImages-1)+".gif")
	self.gifCanvas.create_image(testWidth-100, testHeight/2+20, image = testImage)
	self.gifCanvas.update()
	time.sleep(5)
	self.startButton.config(state=ACTIVE)

def quickSortFunction(self):
	self.startButton.config(state=DISABLED)
	os.chdir("..")
	os.chdir("./QuickSortImages/")
	testImage = PhotoImage(file="tmp-0.gif")
	testWidth=testImage.width()
	testHeight=testImage.height()
	numOfImages = len([name for name in os.listdir('.') if os.path.isfile(name)])
	for num in range (0, numOfImages):
		print (testImage)
		testImage = PhotoImage(file="tmp-"+str(num)+".gif")
		self.gifCanvas.create_image(testWidth-45, testHeight/2+30, image = testImage)
		self.gifCanvas.update()
		time.sleep(timeDelayForBubble)
	testImage = PhotoImage(file="tmp-"+str(numOfImages-1)+".gif")
	self.gifCanvas.create_image(testWidth-45, testHeight/2+30, image = testImage)
	self.gifCanvas.update()
	time.sleep(5)
	self.startButton.config(state=ACTIVE)

def main():
	testVariable = SortMachineGUI()

main()


