from setuptools import find_packages, setup

package_name = 'utilities'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='deepak',
    maintainer_email='deepakkhokhar1313@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'ros_utils_node = utilities.ros_utils:main',
            'math_utils_node = utilities.math_utils:main',
        ],
    },
)
