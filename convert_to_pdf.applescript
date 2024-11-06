-- Prompt user to choose the folder containing .pages files
set theFolder to (choose folder with prompt "Select the folder containing .pages files")

-- Prompt user to choose the destination folder for PDF files
set destinationFolder to (choose folder with prompt "Select the destination folder for PDF files")

tell application "System Events"
    -- Get all .pages files in the selected folder
    set theFiles to path of every file of folder (theFolder as string) whose name extension is "pages"
end tell

repeat with theFile in theFiles
    tell application "Pages"
        -- Open each .pages document
        set theDoc to open file theFile
        
        -- Extract the name without extension
        set theName to text 1 thru -7 of (name of theDoc as string)
        
        -- Create full path for the PDF file in the destination folder
        set pdfFilePath to ((destinationFolder as string) & theName & ".pdf")
        
        -- Export the document as PDF to the specified destination folder
        export theDoc to file pdfFilePath as PDF
        
        -- Close the document without saving changes
        close theDoc saving no
    end tell
end repeat

display alert "Done"