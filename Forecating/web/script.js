document.getElementById('addRow').addEventListener('click', function () {
    const tableBody = document.getElementById('tableBody');
    const newRow = document.createElement('tr');

    newRow.innerHTML = `
        <td><input type="number" name="tahun" placeholder="Tahun"></td>
        <td>
            <select name="quartal">
                <option value="Q1">Q1</option>
                <option value="Q2">Q2</option>
                <option value="Q3">Q3</option>
                <option value="Q4">Q4</option>
            </select>
        </td>
        <td><input type="number" name="aktual" placeholder="Aktual"></td>
        <td><input type="number" name="period" placeholder="Period"></td>
        <td><input type="number" name="alpha" placeholder="Alpha" step="0.01" min="0" max="1"></td>
        <td><input type="number" name="beta" placeholder="Beta" step="0.01" min="0" max="1"></td>
        <td><input type="number" name="gamma" placeholder="Gamma" step="0.01" min="0" max="1"></td>
        <td><button class="deleteRow">Hapus</button></td>
    `;

    tableBody.appendChild(newRow);

    newRow.querySelector('.deleteRow').addEventListener('click', function () {
        tableBody.removeChild(newRow);
    });
});

document.getElementById('submitData').addEventListener('click', function () {
    const rows = document.querySelectorAll('#tableBody tr');
    const data = Array.from(rows).map(row => ({
        tahun: row.querySelector('input[name="tahun"]').value,
        quartal: row.querySelector('select[name="quartal"]').value,
        aktual: row.querySelector('input[name="aktual"]').value,
        period: row.querySelector('input[name="period"]').value,
        alpha: row.querySelector('input[name="alpha"]').value,
        beta: row.querySelector('input[name="beta"]').value,
        gamma: row.querySelector('input[name="gamma"]').value,
    }));

    localStorage.setItem('holtWintersData', JSON.stringify(data));
    window.location.href = 'results.html';
});
