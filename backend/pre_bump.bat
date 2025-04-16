:: Build and update frontend code
cd ../frontend
CALL npm run build:standalone
cd ..
CALL rmdir backend/src/grapycal/webpage
mkdir "backend/src/grapycal/webpage" 
CALL xcopy frontend/dist backend/src/grapycal/webpage /s /e
cd ..