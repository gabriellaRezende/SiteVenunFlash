import { Component, OnInit } from '@angular/core';
import { Product, ProductService } from '../../services/product.service';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import {  RouterLink } from '@angular/router';

@Component({
  selector: 'app-product-list',
  standalone: true,
  imports: [
    CommonModule,
    FormsModule,
    RouterLink
  ],
  templateUrl: './product-list.component.html',
  styleUrl: './product-list.component.css'
})
export class ProductListComponent implements OnInit {
  products: Product[] = [];
  filter = '';

  constructor(private ps: ProductService) {}

  ngOnInit() {
    this.loadAll();
  }

  loadAll() {
    this.ps.getAll().subscribe({
      next: data => this.products = data,
      error: err => console.error('Erro ao carregar produtos', err)
    })
  }

  search() {
    if (this.filter.trim()) {
      this.ps.getByName(this.filter).subscribe(data => this.products = data);
    } else {
      this.loadAll();
    }
  }

}
