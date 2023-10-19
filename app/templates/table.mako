<%inherit file="base.mako"/>
<div class="container py-3">
  	<header class="text-center">
		<h1 class="display-4">Chinook Database</h1>
		<p class="lead mb-0">
			This is <b>Customer table</b> from Chinook Database
		</p>
  	</header>
  	<div class="row py-3">
		<div class="col-lg mx-auto">
			<form id="my-form">
				<input type="text" name="name" id="name">
				<select id="gender" name="gender">
					<option value="foo">Foo</option>
					<option value="bar">Bar</option>
					<option value="baz">Baz</option>
				</select>
				<input type="submit" />
			</form>
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

<%def name="makerow(row)">
    <tr>
    % for key, value in row.items():
        <td>${value}</td>\
    % endfor
    </tr>
</%def>