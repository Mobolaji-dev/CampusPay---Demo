const currencyFormatter = new Intl.NumberFormat('en-NG', {
  style: 'currency',
  currency: 'NGN',
  minimumFractionDigits: 0,
});

function formatCurrency(amount) {
  return currencyFormatter.format(Number(amount || 0));
}

function formatExpiry(value) {
  const date = new Date(value);
  if (Number.isNaN(date.getTime())) return value || 'Unknown';
  const options = { month: 'short', day: 'numeric', hour: '2-digit', minute: '2-digit' };
  return new Intl.DateTimeFormat('en-GB', options).format(date);
}

function loadSuccessDetails() {
  const stored = window.sessionStorage.getItem('latestOrder');
  if (!stored) {
    window.location.href = 'dashboard.html';
    return;
  }

  let order;
  try {
    order = JSON.parse(stored);
  } catch {
    window.location.href = 'dashboard.html';
    return;
  }

  document.getElementById('success-product').textContent = order.name || 'Purchased item';
  document.getElementById('success-vendor').textContent = order.vendor_name || order.vendor_id || 'Unknown vendor';
  document.getElementById('success-total').textContent = formatCurrency(order.total_charged);
  document.getElementById('success-order').textContent = order.order_id || 'N/A';
  document.getElementById('success-expiry').textContent = formatExpiry(order.timer_expire_at);
}

document.addEventListener('DOMContentLoaded', () => {
  loadSuccessDetails();

  document.getElementById('verify-btn').addEventListener('click', () => {
    window.location.href = 'receipt.html';
  });

  document.getElementById('continue-btn').addEventListener('click', () => {
    window.location.href = 'dashboard.html';
  });
});
