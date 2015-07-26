#!/usr/bin/env python3

import argparse

class Implication():
    def __init__(self, keyword, category):
        self.keyword = keyword
        self.category = category
    def implies(self, word): # Just slightly easier, don't judge
        return word == self.keyword
    
class Category():
    def __init__(self, name):
        self.name = name
        self.counter = 0
    def increment(self):
        self.counter += 1
        
class Categories():
    def __init__(self):
        self.categories = []
    def append(self, category):
        for category in self.categories:
            if category.name == catName:
                pass
        self.categories.append(category)
    def increment(self, catName):
        for category in self.categories:
            if category.name == catName:
                category.increment()
                return True
        return False

def main(args):
    # Get command line arguments
    setVerbose = args.verbose
    fileName = args.file
    outName = args.output
    implicationName = args.implication
    restrainWord = args.restrain

    implications = []
    categories = Categories()

    # Scan implications
    implicationFile = open(implicationName, 'r')
    for implicationPair in implicationFile:
        keyword, catName= implicationPair.split()
        implication = Implication(keyword, catName)
        implications.append(implication)
        category = Category(catName)
        categories.append(category)
        if setVerbose:
            print("Keyword %s implies category %s" % (keyword, catName))

    # Start scanning file
    scanFile = open(fileName, 'r')
    saveFile = open(outName, 'w')
    for line in scanFile:
        print("Line: %s" % line)
        if not restrainWord in line:
            if setVerbose:
                print('Skipping line: %s' % line)
                # Write line plain
                saveFile.write(line)
            continue
        # Split all the words
        words = line.split()
        # We keep a boolean file to track if this line is already categorized
        lineDone = False
        for word in words:
            for implication in implications:
                if implication.implies(word):
                    print("Detected category is %s. Press ENTER to confirm." % implication.category)
                    userConfirm = input()
                    if userConfirm == '':
                        # Write out to file
                        outLine = implication.category+ " " + line
                        saveFile.write(outLine)
                        categories.increment(implication.category)
                        lineDone = True
                        pass
                    else:
                        if setVerbose:
                            print('Skipping keyword: %s' % word)
                else:
                    continue
        while not lineDone:
            print("Please input category name:")
            catName = input()
            if catName == '':
                continue
            lineDone = True
            # Write out to file
            outLine = catName + " " + line
            saveFile.write(outLine)
            incremented = categories.increment(catName)
            if not incremented:
                if setVerbose:
                    print('Adding new category: %s' % catName)
                category = Category(catName)
                categories.append(category)
                categories.increment(catName)
    print('Report:')
    for category in categories.categories:
        print("Category %s: %i" % (category.name, category.counter))
    pass

# Run main if not loaded as a module
if __name__ == '__main__':
    # Create a parser to handle command line arguments
    parser = argparse.ArgumentParser(description='Changelog analysis tool.')
    parser.add_argument('-f', '--file', help='Changelog file', required=True)
    parser.add_argument('-o', '--output', help='Output file', required=True)
    parser.add_argument('-i', '--implication', help='Implication table file', required=True)
    parser.add_argument('-r', '--restrain', help='Changelog identification character', required=True)
    parser.add_argument('-v', '--verbose', help='Verbose logging', action='store_true')
    args = parser.parse_args()
    # Call the main
    quit(main(args))
