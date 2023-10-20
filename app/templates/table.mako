<%inherit file="base.mako"/>
<div class="container py-3">
  	<header class="text-center">
		<h1 class="display-4">Chinook Database</h1>
		<p class="lead mb-0">
			This is <b>${table} table</b> from Chinook Database
		</p>
		<br>
		<p>
			Our you go back <a href="/">Home</a>
		</p>
  	</header>
  	<div class="row py-3">
		<div class="col-lg mx-auto">
			<div class="card rounded shadow border-0">
				<div class="card-body p-5 bg-white rounded">
					<form id="my-form">
						<span>Column</span>
						<select id="column" name="filterColumn">
							% for header in headers:
								%if header == column:
									<option value="${header}" selected>${header}</option>
								%else:
									<option value="${header}">${header}</option>
								%endif
							% endfor
						</select>
						<span>Value</span>
						%if not value:
							<input type="text" name="filterValue" id="value">
						%else:
							<input type="text" name="filterValue" id="value" value="${value}">
						%endif
						<input type="submit" class="btn btn-primary" />
						<button type="button" class="btn btn-primary" id="clearButton">Clear</button>
					</form>
				</div>
			</div>
		</div>
		<div class="col-lg mx-auto">
			<div class="card rounded shadow border-0">
				<div class="card-body p-5 bg-white rounded">
					<div class="table-responsive">
						<table id="example" style="width:100%" class="table table-striped table-bordered">
							<thead>
								<tr>
								% for header in headers:
									<th>${header}</th>
								% endfor
								</tr>
							</thead>
							<tbody>
							% for row in rows:
								${makerow(row)}
							% endfor
							</tbody>
						</table>
					</div>
				</div>
			</div>
		</div>
	</div>
</div>

<script>
	const form = document.getElementById('my-form');

	form.addEventListener('submit', (evt) => {
		evt.preventDefault();
		const formData = new FormData(form);
		const params = new URLSearchParams(formData);
		var column = params.get("filterColumn");
		var value = params.get("filterValue");
		var url = "/db/Chinook/${table}/" + column + "/" + value + ".html"
		console.log(url.toString());
		window.location.href = url;
	});

	document.getElementById("clearButton").onclick = function(e){
		e.preventDefault();
		window.location = "/db/Chinook/${table}.html";    
	};
</script>

<%def name="makerow(row)">
    <tr>
    % for key, value in row.items():
        <td>${value}</td>\
    % endfor
    </tr>
</%def>