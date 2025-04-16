Install https://github.com/commitizen-tools/commitizen

1. check the version of objectsync and topicsync is the newest
1. update the version information in frontend\src\version.ts and frontend\package.json
1. temporary copy readme.md to backend\readme.md so that it can be published
1. Go to "/backend" folder and bump version with `cz bump` 
1. Go to "/" folder and run `pip install -e backend -e extensions\grapycal_builtin`
1. update and copy the example file to backend\src\grapycal\Welcome.grapycal
1. poerty build with `build.bat`
1. delete grapycal config file in appdata
1. test_build.bat 
1. publish: `publish.bat`
1. test_build_pypi.bat 
1. update and push the example files
