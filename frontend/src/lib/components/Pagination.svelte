<script lang="ts">
  interface Props {
    currentPage: number;
    totalPages: number;
    onPageChange: (page: number) => void;
  }

  let { currentPage, totalPages, onPageChange }: Props = $props();

  function goToPage(page: number) {
    if (page >= 1 && page <= totalPages && page !== currentPage) {
      onPageChange(page);
    }
  }

  function prevPage() {
    if (currentPage > 1) {
      onPageChange(currentPage - 1);
    }
  }

  function nextPage() {
    if (currentPage < totalPages) {
      onPageChange(currentPage + 1);
    }
  }

  // Generate page numbers to show
  function getPageNumbers() {
    const pages: number[] = [];
    const maxVisible = 5;
    
    if (totalPages <= maxVisible) {
      // Show all pages if total is small
      for (let i = 1; i <= totalPages; i++) {
        pages.push(i);
      }
    } else {
      // Show first, last, and pages around current
      if (currentPage <= 3) {
        for (let i = 1; i <= 4; i++) pages.push(i);
        pages.push(-1); // Ellipsis
        pages.push(totalPages);
      } else if (currentPage >= totalPages - 2) {
        pages.push(1);
        pages.push(-1); // Ellipsis
        for (let i = totalPages - 3; i <= totalPages; i++) pages.push(i);
      } else {
        pages.push(1);
        pages.push(-1); // Ellipsis
        for (let i = currentPage - 1; i <= currentPage + 1; i++) pages.push(i);
        pages.push(-1); // Ellipsis
        pages.push(totalPages);
      }
    }
    
    return pages;
  }
</script>

{#if totalPages > 1}
  <div class="flex items-center justify-center gap-2 mt-8">
    <!-- Previous Button -->
    <button
      onclick={prevPage}
      disabled={currentPage === 1}
      class="px-4 py-2 rounded-lg border border-gray-300 bg-white text-gray-700 font-medium hover:bg-gray-50 disabled:opacity-50 disabled:cursor-not-allowed transition-colors"
    >
      Previous
    </button>

    <!-- Page Numbers -->
    <div class="flex items-center gap-1">
      {#each getPageNumbers() as page}
        {#if page === -1}
          <span class="px-3 py-2 text-gray-500">...</span>
        {:else}
          <button
            onclick={() => goToPage(page)}
            class="min-w-[40px] px-3 py-2 rounded-lg border font-medium transition-colors {currentPage === page
              ? 'bg-sky-500 text-white border-sky-500'
              : 'border-gray-300 bg-white text-gray-700 hover:bg-gray-50'}"
          >
            {page}
          </button>
        {/if}
      {/each}
    </div>

    <!-- Next Button -->
    <button
      onclick={nextPage}
      disabled={currentPage === totalPages}
      class="px-4 py-2 rounded-lg border border-gray-300 bg-white text-gray-700 font-medium hover:bg-gray-50 disabled:opacity-50 disabled:cursor-not-allowed transition-colors"
    >
      Next
    </button>
  </div>
{/if}

