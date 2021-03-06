import setuptools

with open("README.md", "r") as fh:
	long_description = fh.read()

setuptools.setup(
	name = 'cardiopy',
	version = "0.0.5",
	author = "Jackie Gottshall",
	author_email = "jackie.gottshall@gmail.com",
	description = "Analysis package for single-lead clinical EKG data",
	long_description = long_description,
	long_description_content_type = "text/markdown",
	url="https://github.com/CardioPy/CardioPy",
	packages = setuptools.find_packages(),
	classifiers = [
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: BSD License",
		"Operating System :: OS Independent",
		"Intended Audience :: Science/Research",
		"Topic :: Scientific/Engineering :: Medical Science Apps."
		],
	python_requires = '>=3.6',
	install_requires = [
		"datetime",
		"matplotlib",
		"pandas",
		"scipy",
		"statistics",
		"mne",
		"numpy"
	]
	)
