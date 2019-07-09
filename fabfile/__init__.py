import sys

if 'fab' in sys.argv[0]:
    from edc_fabric import fabfile as common
    from edc_fabric.fabfile.git import cut_releases, generate_requirements
