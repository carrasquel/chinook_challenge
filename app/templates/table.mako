<%inherit file="base.mako"/>
<div class="container py-5">
  	<header class="text-center">
		<h1 class="display-4">Bootstrap Datatables</h1>
		<p class="lead mb-0">Using Bootstrap 4 and <a href="https://datatables.net/examples/styling/bootstrap4.html" class="font-italic">
			<u>Datatables</u></a>, add interaction controlsto your HTML tables.</p>
		<p class="font-italic">Snippet By
		<a href="https://bootstrapious.com">
			<u>Bootstrapious</u>
		</a>
		</p>
  	</header>
  	<div class="row py-5">
		<div class="col-lg-10 mx-auto">
			<div class="card rounded shadow border-0">
				<div class="card-body p-5 bg-white rounded">
					<div class="table-responsive">
						<table id="example" style="width:100%" class="table table-striped table-bordered">
							% for row in rows:
								${makerow(row)}
							% endfor
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