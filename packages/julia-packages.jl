using Pkg

printstyled("Updating metadata:\n", color=:cyan)
Pkg.update()

printstyled("Running build scripts:\n", color=:cyan)
Pkg.build()

packages = (
    "IJulia",
    "GR",
    "Plots",
    "StatPlots",
    "IterTools",
    "DataFrames",
    "HDF5",
    "PyCall",
    "RCall",
    "RDatasets",
    "DataFrames",
    "ScikitLearn",
    "Gadfly",
    "LibPQ",
    "Makie",
    "PlotlyJS"
)

for p = packages
    printstyled("Installing $p:\n", color=:cyan)
    Pkg.add(p)
end

function recompile_packages()
    for pkg in keys(Pkg.installed())
        try
            @info("Compiling: $pkg")
            eval(Expr(:toplevel, Expr(:using, Symbol(pkg))))
        catch err
            @warn("Unable to precompile: $pkg")
            @warn(err)
        end
    end
end

printstyled("Precompiling:\n", color=:cyan)
recompile_packages()
printstyled("Done.\n", color=:green)
