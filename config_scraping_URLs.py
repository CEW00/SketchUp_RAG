import os

current_dir = os.path.dirname(os.path.abspath(__file__))

source_path = os.path.join(current_dir, "books")

# Define the paths to source files
file_paths = [
    os.path.join(current_dir, "books", "sketchup_concepts.pdf"),
    os.path.join(current_dir, "books", "sketchup_userguide.pdf"),
    os.path.join(current_dir, "books", "scraped_data.json"),
]


# Define the URLs for each difficulty level
easy_urls = [
    'https://designerhacks.com/how-to-create-sections-in-sketchup/',
    'https://designerhacks.com/how-to-stop-clipping-in-sketchup/',
    'https://designerhacks.com/how-to-get-rid-of-duplicate-shadows-in-sketchup/',
    'https://designerhacks.com/how-to-draw-2d-in-sketchup/',
    'https://designerhacks.com/how-to-make-an-architectural-2d-elevation-in-sketchup/',
    'https://designerhacks.com/mass-select-components-in-sketchup/',
    'https://designerhacks.com/how-to-add-materials-in-sketchup/',
    'https://designerhacks.com/getting-started-with-sketchup-for-beginners/',
    'https://designerhacks.com/stop-doing-this-with-your-sketchup-site-models/',
    'https://designerhacks.com/5-sketchup-mistakes-every-beginner-makes-and-how-to-avoid-them/',
    'https://designerhacks.com/how-to-get-essential-site-information-for-architecture-projects/',
    'https://designerhacks.com/how-to-snap-in-sketchup-tutorial/',
    'https://designerhacks.com/how-to-create-faces-automatically-sketchup-create-faces-q-a/',
    'https://designerhacks.com/how-to-quickly-convert-an-autocad-dwg-to-3d-in-sketchup/',
    'https://designerhacks.com/how-to-reduce-sketchup-file-size/',
    'https://designerhacks.com/how-to-import-components-in-the-sketchup-web-app/',
    'https://designerhacks.com/sketchup-scenes-tutorial/',
    'https://designerhacks.com/export-files-from-sketchup-to-stl/',
    'https://designerhacks.com/how-to-make-sketchup-shortcuts/',
    'https://designerhacks.com/install-sketchup/',
    'https://designerhacks.com/polygons-sketchup/',
    'https://designerhacks.com/3d-text-sketchup-create-move-manipulate/',
    'https://designerhacks.com/install-sketchup-plugins-extensions-increase-productivity/',
    'https://designerhacks.com/sketchup2014/',
    'https://designerhacks.com/sketchupgooglemaps/',
    'https://designerhacks.com/find-use-sketchups-dynamic-components/',
    'https://designerhacks.com/get-the-google-sketchup-free-download/',
    'https://designerhacks.com/getting-started-sketchup/',
    'https://designerhacks.com/sketchup-filesize-the-impact-of-groups-and-components/'
]

medium_urls = [
    'https://designerhacks.com/how-to-convert-objects-to-low-poly-in-sketchup/',
    'https://designerhacks.com/how-to-make-windows-in-sketchup/',
    'https://designerhacks.com/how-to-model-ikea-furniture-in-sketchup/',
    'https://designerhacks.com/getting-rid-of-ghosting-lines-in-sketchup/',
    'https://designerhacks.com/how-to-design-a-sloped-wall-in-sketchup/',
    'https://designerhacks.com/how-to-draw-lines-on-terrain-sketchup-tutorial/',
    'https://designerhacks.com/creating-a-curved-cutout-in-sketchup-sketchup-qa/',
    'https://designerhacks.com/creating-engraved-or-embedded-text-in-sketchup/',
    'https://designerhacks.com/how-to-make-an-angled-cut-in-sketchup-sketchup-q-a/',
    'https://designerhacks.com/how-to-import-and-edit-stl-files-in-sketchup/',
    'https://designerhacks.com/saki-house-sketchup-speed-model-lumion-9-render/',
    'https://designerhacks.com/how-to-soften-edges-and-round-corners-in-sketchup/',
    'https://designerhacks.com/how-to-create-domes-in-sketchup/',
    'https://designerhacks.com/sketch-floor-plan-to-3d-in-sketchup/',
    'https://designerhacks.com/from-concept-to-3d-in-sketchup/',
    'https://designerhacks.com/7-of-the-best-sketchup-plugins/',
    'https://designerhacks.com/how-to-align-objects-in-sketchup-the-easy-way/',
    'https://designerhacks.com/how-to-create-a-sphere-in-sketchup/',
    'https://designerhacks.com/how-to-push-pull-curved-surfaces-in-sketchup/',
    'https://designerhacks.com/how-to-generate-a-contour-map-with-sketchup/',
    'https://designerhacks.com/how-to-change-units-in-sketchup/',
    'https://designerhacks.com/how-to-import-a-dwg-to-sketchup-without-pro/',
    'https://designerhacks.com/how-to-use-the-sketchup-follow-me-tool/',
    'https://designerhacks.com/how-to-export-a-dwg-from-sketchup/',
    'https://designerhacks.com/sketchup-unfold/',
    'https://designerhacks.com/5-quick-tips-to-getting-started-with-sketchup-layout/',
    'https://designerhacks.com/sketchup-complex-curves/',
    'https://designerhacks.com/simple-ways-customize-sketchup-images-every-design/',
    'https://designerhacks.com/avoid-sketchup-bug-splat/',
    'https://designerhacks.com/embed-sketchup-models-3dwarehouse-onto-portfolio-site/',
    'https://designerhacks.com/import-sketchup-textures-create-custom-materials/',
    'https://designerhacks.com/create-sphere-dome-curved-shape-sketchup/',
    'https://designerhacks.com/setup-photo-matching-sketchup/',
    'https://designerhacks.com/5-essential-sketchup-plugins/',
    'https://designerhacks.com/5-reasons-creating-local-sketchup-library/'
]

hard_urls = [
    'https://designerhacks.com/how-to-create-a-beautiful-line-rendering-with-sketchup-and-vray/',
    'https://designerhacks.com/7-ways-to-make-money-with-sketchup/',
    'https://designerhacks.com/futuristic-sketchup-interior-design-sketchup-speed-model-lumion-9-render/',
    'https://designerhacks.com/moon-house-sketchup-speed-model/',
    'https://designerhacks.com/dealing-with-sketchup-error-number-of-segments-too-large/',
    'https://designerhacks.com/how-to-add-texture-to-a-curved-surface-in-sketchup/',
    'https://designerhacks.com/how-to-create-realistic-grass-with-vray-in-sketchup/',
    'https://designerhacks.com/creating-a-parametric-design-in-sketchup-with-viz-pro/',
    'https://designerhacks.com/how-to-get-area-calculations-in-sketchup/',
    'https://designerhacks.com/how-to-import-from-blender-to-sketchup/',
    'https://designerhacks.com/using-sketchup-for-architecture-design-workflow/',
    'https://designerhacks.com/how-to-turn-2d-typography-or-a-survey-to-3d-terrain-in-sketchup/',
    'https://designerhacks.com/how-to-create-sketchup-topography/',
    'https://designerhacks.com/how-to-3d-model-from-a-photo-sketchup/',
    'https://designerhacks.com/5-unconventional-sketchup-tips-might-know/',
    'https://designerhacks.com/speedupsketchup/'
]