
> I assume you are in the main repository folder



## get a working node js version

One option to do this is to create a conda environment and install nodejs into 
a new environment

```cmd
conda create -n isbm2021hack nodejs
conda activate isbm2021hack
```

To continue you should have the node package manager (npm) available.

```cmd
npm --version
```

## install required node packages

```cmd
npm install three jquery axios querystring
# install from github does not seem to work
# npm install git://github.com/ncbi/icn3d
npm install icn3d
```

