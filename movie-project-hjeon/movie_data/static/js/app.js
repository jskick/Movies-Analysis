// Plot the default route once the page loads
var defaultURL = "/profit";
d3.json(defaultURL).then(function(data) {
  var data = [data];
  var layout = {
	  autosize: true,
	  xaxis: {
		  automargin: true
	  }
  };
  Plotly.plot("bar", data, layout);
});

// Update the plot with new data
function updatePlotly(newdata) {
  Plotly.restyle("bar", "x", [newdata.x]);
  Plotly.restyle("bar", "y", [newdata.y]);
}

// Get new data whenever the dropdown selection changes
function getData(route) {
  console.log(route);
  d3.json(`/${route}`).then(function(data) {
    console.log("newdata", data);
    updatePlotly(data);
  });
}
