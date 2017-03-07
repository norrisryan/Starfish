# The files output by the plot_structure command
STRUCT := $(shell starfish_plot_data.py -M)

# The files output by the starfish_initialize.jl command
# Read the dependencies from the program itself
OBJS := $(shell starfish_initialize.py -M)

# Generate the data.hdf5 file
.PHONY : structure
.NOTPARALLEL : structure
structure : $(STRUCT)

$(STRUCT) : config.yaml
	starfish_plot_data.py

.NOTPARALLEL : $(OBJS)
$(OBJS) : config.yaml
	starfish_initialize.py

data.hdf5 : $(OBJS)
	starfish_grid.py --create

.PHONY : chmaps
chmaps : chmaps_linear.png chmaps_log.png

chmaps_linear.png : image.out
	DJ_plot_chmaps.jl --linear

chmaps_log.png : image.out
	DJ_plot_chmaps.jl --log

spectrum.png : image.out
	DJ_plot_chmaps.jl --spectrum

# Make the visibilities for both the model and residuals.
.NOTPARALLEL : vis
.PHONY : vis
vis : model.hdf5 resid.hdf5

model.hdf5 resid.hdf5 : image.out
	DJ_write_model.jl

all: structure chmaps spectrum.png vis

.PHONY: clean
clean:
	$(RM) $(OBJS)
	$(RM) $(STRUCT)
	$(RM) image.out
	$(RM) radmc3d.out
	$(RM) chmaps_linear.png
	$(RM) chmaps_log.png
	$(RM) chmaps_blur.png
	$(RM) spectrum.png
	$(RM) model.hdf5
	$(RM) resid.hdf5
