import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ListSpecialitiesComponent } from './list-specialities.component';

describe('ListSpecialitiesComponent', () => {
  let component: ListSpecialitiesComponent;
  let fixture: ComponentFixture<ListSpecialitiesComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ListSpecialitiesComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ListSpecialitiesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
